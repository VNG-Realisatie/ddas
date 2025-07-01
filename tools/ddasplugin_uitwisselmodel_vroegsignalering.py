import logging

import crunch_uml.util as util
from crunch_uml.db import Association, Attribute, Class
from crunch_uml.exceptions import CrunchException
from crunch_uml.transformers.plugin import Plugin

logger = logging.getLogger()

VROEGSIGNALERING_PACKAGE_ID = "EAPK_BB7B01A9_44F5_4e0f_B158_0DDAA5B6593D"
VROEGSIGNAAL_ID = "EAID_C6DA2586_C0E3_4868_93E8_64AF6D118092"  # C6DA2586-C0E3-4868-93E8-64AF6D118092}
UITWISSELMODEL_ID = "EAID_6b4326e3_eb4e_41d2_902b_44ff06604f63"
CLIENT_ID = "EAID_DAF09055_A5A6_4ff4_A158_21B20567B296"
TRAJECTEN_SORT_ORDER = [
    'signaalpartner',
    'vroegsinaalzaak'
]



class DDASPluginUitwisselmodel(Plugin):
    def transformLogic(self, args, root_package, schema_from, schema_to):
        logger.info("Starting DDAS Uitwisselmodel Plugin voor vroegsignalering")
        # Clean up
        schema_to.clean()

        if not root_package.id == VROEGSIGNALERING_PACKAGE_ID:
            msg = (
                f"Cannot transform using {self.__class__.__name__}: Root package is needs to be model"
                f" schuldhulpverlening with id {VROEGSIGNALERING_PACKAGE_ID}."
            )
            logger.error(msg)
            raise CrunchException(msg)

        # Kopie schuldhulpverlening model
        kopie = root_package.get_copy(None, materialize_generalizations=True)

        # Now remove all associations with name 'resulteert in'
        #for clazz in kopie.classes:
        #    lst_assoc = [assoc for assoc in clazz.uitgaande_associaties]
        #    for association in lst_assoc:
        #        if str(association.name).strip() in [
        #            "resulteert in",
        #            "dienstverlening",
        #            "voert traject uit",
        #            "soort",
        #            "heeft financiele situatie",
        #        ]:
        #            clazz.uitgaande_associaties.remove(association)

        # Zet de onderdelen van het traject in de juiste volgorde
        sort_order = [item.lower() for item in TRAJECTEN_SORT_ORDER if isinstance(item, str)]
        for clazz in kopie.classes:
            if str(clazz.name).strip() == "Vroegsignaal":
                for association in clazz.uitgaande_associaties:
                    dst_class = schema_from.get_class(association.dst_class_id)
                    if dst_class:
                        dst_name = str(dst_class.name).strip().lower()
                        if dst_name in sort_order:
                            association.order = sort_order.index(dst_name) + 1
                        else:
                            association.order = 100


        # Now remove classes 'project', 'projectsoort' en 'notariele status'
        #for clazz in kopie.classes:
        #    if str(clazz.name).strip() in [
        #        "Huishouden",
        #        "Partner",
        #        "Inkomen",
        #        "Woningbezit",
        #        "Ondernemer",
        #    ]:  # or str(clazz.name).strip() == "Projectsoort" or str(clazz.name).strip() == "Notariele status"
        #        kopie.classes.remove(clazz)

        # Now add the Class Uitwisselmodel
        uitwisselmodel = Class(
            id=UITWISSELMODEL_ID,
            name="Uitwisselmodel",
            schema_id=schema_to.schema_id,
            package=kopie,
            definitie=(
                "Het uitwisselmodel is een model dat de gegevens bevat die uitgewisseld worden tussen de verschillende"
                " partijen."
            ),
        )
        startdatumLevering = Attribute(
            id=util.getEAGuid(),
            name="startdatumLevering",
            schema_id=schema_to.schema_id,
            primitive="Datum",
            verplicht=True,
            definitie="De begindatum van de periode waarover gerapporteerd wordt binnen de levering",
        )
        einddatumLevering = Attribute(
            id=util.getEAGuid(),
            name="einddatumLevering",
            schema_id=schema_to.schema_id,
            primitive="Datum",
            verplicht=True,
            definitie="De einddatum van de periode waarover gerapporteerd wordt binnen de levering",)
        aanleverdatumEnTijd = Attribute(
            id=util.getEAGuid(),
            name="aanleverdatumEnTijd",
            schema_id=schema_to.schema_id,
            primitive="datumtijd",
            verplicht=True,
            definitie="De datum en tijd waarop de gegevens zijn aangeleverd.",)
        codeGegevensleverancier = Attribute(
            id=util.getEAGuid(),
            name="codeGegevensleverancier",
            schema_id=schema_to.schema_id,
            definitie="Code van de gegevensleverancier (softwareleverancier of hosting partij) die de gegevens voor 1 of meer partijen levert.",
            verplicht=True,
            primitive="AN200",
        )

        uitwisselmodel.attributes.append(startdatumLevering)
        uitwisselmodel.attributes.append(einddatumLevering)
        uitwisselmodel.attributes.append(aanleverdatumEnTijd)
        uitwisselmodel.attributes.append(codeGegevensleverancier)

        assoc_uitmod_to_vroegsignaal = Association(
            id=util.getEAGuid(),
            name="bevat",
            schema_id=schema_to.schema_id,
            src_class_id=uitwisselmodel.id,
            dst_class_id=VROEGSIGNAAL_ID,
            dst_mult_start="1",
            dst_mult_end="-1",
            src_role="vroegsignalen",
            definitie="De vroegsignalen die in het uitwisselmodel zijn opgenomen.",
            order=1,
        )
        uitwisselmodel.uitgaande_associaties.append(assoc_uitmod_to_vroegsignaal)

        kopie.classes.append(uitwisselmodel)
        schema_to.add(kopie, recursive=True)

        logger.info("DDAS Uitwisselmodel voor vroegsignalering Plugin finished.")
