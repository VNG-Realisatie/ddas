import logging

import crunch_uml.util as util
from crunch_uml.db import Association, Attribute, Class
from crunch_uml.exceptions import CrunchException
from crunch_uml.transformers.plugin import Plugin

logger = logging.getLogger()

VROEGSIGNALERING_PACKAGE_ID = "EAPK_BB7B01A9_44F5_4e0f_B158_0DDAA5B6593D"
VROEGSIGNAAL_ID = "EAID_C6DA2586_C0E3_4868_93E8_64AF6D118092"  # C6DA2586-C0E3-4868-93E8-64AF6D118092}
VROEGSIGNAALZAAK_ID = "EAID_1AA67F0D_3B94_48a3_A037_A2ACC6D61CF0"  # 839017B2-0F95-42d0-AB2B-E873636340DA
UITWISSELMODEL_ID = "EAID_6b4326e3_eb4e_41d2_902b_44ff06604f63"
CLIENT_ID = "EAID_DAF09055_A5A6_4ff4_A158_21B20567B296"
AANLEVERENDEORGANISATIE = "EAID_3109FEF3_A1CB_4f50_800B_376A18465F9F"
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

        # Add the class Levering
        levering = Class(
            id=util.getEAGuid(),
            name="Levering",
            schema_id=schema_to.schema_id,
            package=kopie,
            definitie=(
                "Een levering bevat steeds van één gemeente de verzameling van vroegsignalen en vroegsignaalzaken"
                " die over een bepaalde periode worden aangeleverd."
            ),
        )
        levering.attributes.append(Attribute(
                id=util.getEAGuid(),
                name="teller",
                schema_id=schema_to.schema_id,
                primitive="int",
                verplicht=True,
                definitie="Teller van het aantal leveringen dat in het bestand is opgenomen.",
            )
        )
        levering.attributes.append(Attribute(
                id=util.getEAGuid(),
                name="gemeentecode",
                schema_id=schema_to.schema_id,
                definitie="Code van de gemeente names wie de levering is gedaan.",
                verplicht=True,
                primitive="AN6",
            )
        )
        assoc_uitmod_to_levering = Association(
            id=util.getEAGuid(),
            name="is van",
            schema_id=schema_to.schema_id,
            src_class_id=uitwisselmodel.id,
            dst_class_id=levering.id,
            dst_mult_start="1",
            dst_mult_end="-1",
            src_role="leveringen",
            definitie="De leveringen die in het uitwisselmodel zijn opgenomen.",
            order=1,
        )
        assoc_uitmod_to_levering.order = 1
        uitwisselmodel.uitgaande_associaties.append(assoc_uitmod_to_levering)
        assoc_uitmod_to_levering.dst_class = levering

        assoc_levering_to_organisatie = Association(
            id=util.getEAGuid(),
            name="organisatie",
            schema_id=schema_to.schema_id,
            src_class_id=levering.id,
            dst_class_id=AANLEVERENDEORGANISATIE,
            dst_mult_start="1",
            dst_mult_end="1",
            src_role="aanleverende_organisatie",
            definitie="De organisatie die de gegevens volgens het uitwisselmodel aanlevert.",
            order=1,
        )
        assoc_levering_to_organisatie.order = 1
        levering.uitgaande_associaties.append(assoc_levering_to_organisatie)


        # Zet vroegsignalen als eerste in uitwisselspecificatie
        assoc_uitmod_to_vroegsignaal = Association(
            id=util.getEAGuid(),
            name="bevat",
            schema_id=schema_to.schema_id,
            src_class_id=levering.id,
            dst_class_id=VROEGSIGNAAL_ID,
            dst_mult_start="0",
            dst_mult_end="-1",
            src_role="vroegsignalen",
            definitie="De vroegsignalen die in het uitwisselmodel zijn opgenomen.",
            order=2,
        )
        levering.uitgaande_associaties.append(assoc_uitmod_to_vroegsignaal)

        # Zet vroegsignaalzaken als tweede in uitwisselspecificatie
        assoc_uitmod_to_vroegsignaalzaak = Association(
            id=util.getEAGuid(),
            name="bevat",
            schema_id=schema_to.schema_id,
            src_class_id=levering.id,
            dst_class_id=VROEGSIGNAALZAAK_ID,
            dst_mult_start="0",
            dst_mult_end="-1",
            src_role="vroegsignaalzaken",
            definitie="De vroegsignaalzaken die in het uitwisselmodel zijn opgenomen.",
            order=3,
        )
        levering.uitgaande_associaties.append(assoc_uitmod_to_vroegsignaalzaak)

        # Now remove association between vroegsignaal en zaak, anders toont uitwisselmodel zaken niet
        # Haal de vroegsignaal en vroegsignaalzaak classes op uit de kopie
        for clazz in kopie.classes:
            lst_assoc = [assoc for assoc in clazz.uitgaande_associaties]
            for association in lst_assoc:
                if str(association.name).strip() in [
                    "opgepaktIn",
                ]:
                    clazz.uitgaande_associaties.remove(association)
            if clazz.id == VROEGSIGNAAL_ID:
                vroegsignaal = clazz
            if clazz.id == VROEGSIGNAALZAAK_ID:
                vroegsignaalzaak = clazz

        # Maak nu de referenties vanuit de zaken aan naar de vroegsignalen. Hiervoor maken we een referentieclass aan met ID
        # vroegsignaalzaak en vroegsignaal, zodat we vanuit de vroegsignaalzaak naar het vroegsignaal kunnen verwijzen. 
        # Geef het vroegsignaal een ID om vanuit Vroegsignaalzaak naartoe te kunnen verwijzen
        logger.info("Copying the client package.")
        vroegsignaal.attributes.insert(
            0,
            Attribute(
            id=util.getEAGuid(),
            name="ID",
            schema_id=schema_to.schema_id,
            primitive="AN200",
            verplicht=True,
            )
        )
        # Now add the Class Uitwisselmodel
        vroegsignaal_ref = Class(
            id=util.getEAGuid(),
            name="Vroegsignaal",
            schema_id=schema_to.schema_id,
            package=kopie,
            definitie=(
                "Referentie naar het vroegsignaal dat hoort bij de vroegsignaalzaak. "
            ),
        )
        vroegsignaal_ref.attributes.append(
            Attribute(
                id=util.getEAGuid(),
                name="ID",
                schema_id=schema_to.schema_id,
                primitive="AN200",
                verplicht=True,
            )
        )
        assoc_vroegsignaalzaak_to_vroegsignaalref = Association(
            id=util.getEAGuid(),
            name="opgeklaptIn",
            schema_id=schema_to.schema_id,
            src_class_id=vroegsignaalzaak.id,
            dst_class_id=vroegsignaal_ref.id,
            dst_mult_start="1",
            dst_mult_end="-1",
            src_role="vroegsignalen",
            definitie="De lijst ID's van de vroegsignalen op basis waarvan de vroegsignaalzaak is geopend.",
            order=2,
        )
        vroegsignaalzaak.uitgaande_associaties.append(assoc_vroegsignaalzaak_to_vroegsignaalref)
        # Einde referentieclass aanmaken



        kopie.classes.append(uitwisselmodel)
        schema_to.add(kopie, recursive=True)

        logger.info("DDAS Uitwisselmodel voor vroegsignalering Plugin finished.")
