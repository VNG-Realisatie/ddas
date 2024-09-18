#!/usr/bin/env bash
XMI="./data/Gemeentelijk Gegevensmodel XMI2.1.xml"
JSON="./$1/json_schema.json"
MD="./docs/Detail.md"
ROOT_SCHULDHULP=EAPK_06C51790_1F81_4ac4_8E16_5177352EF2E1
ROOT_CLASS_UITWISSELMODEL=EAID_6b4326e3_eb4e_41d2_902b_0bff06604f63
UITWISSEL_TEMPLATE=./docs/uitwisselspecificatie.md.template
UITWISSEL_MD=./docs/uitwisselspecificatie.md


echo "Script to read datamodel from $XMI and generate JSON Schema and Markdown documentation for the version entered on the command line"

# Check if the version parameter is provided
if [ -z "$1" ]; then
    echo "Please provide a version number for this release."
    exit 1
fi
# Check if the version parameter has the correct format
if [[ ! $1 =~ ^v[0-9]+\.[0-9]+$ ]]; then
    echo "Invalid version number format. Please provide a version number in the format v{number}.{number} like v0.9 or v1.11"
    exit 1
fi
version="$1"
JSON="./$version/json_schema.json"

# Controleer of het temp.md.template bestand bestaat
if [ ! -f "$UITWISSEL_TEMPLATE" ]; then
    echo "File $UITWISSEL_TEMPLATE does not exist."
    exit 1
fi

# Check if crunch_uml is installed
if ! command -v crunch_uml &> /dev/null; then
    echo "This tool makes use of crunch_uml, but is not installed. Please install crunch_uml before proceeding. See: https://github.com/brienen/crunch_uml"
    exit 1
fi
# Check if mkdocs is installed
if ! command -v mkdocs &> /dev/null; then
    echo "This tool makes use of mkdocs, but is not installed. Please install mkdocs before proceeding. See: https://www.mkdocs.org"
    exit 1
fi
# Check if mike is installed
if ! command -v mike &> /dev/null; then
    echo "This tool makes use of mike for versioned documentation, but is not installed. Please install mike before proceeding. See: https://github.com/jimporter/mike"
    exit 1
fi
# Check if the directory with the name of the version exists
if [ ! -d "$version" ]; then
    # Create the directory if it doesn't exist
    mkdir "$version"
    echo "Created directory $version"
fi


# First read the XMI
echo "Reading GGM Datamodel $XMI..."
crunch_uml import -f "$XMI" -t eaxmi -db_create

# Peform transformation and move schuldhulp module to crunch-schema 'schuldhulp_informatiemodel'
echo "Extracting and tranforming schuldhulp datamodel..."
crunch_uml transform -ttp plugin -sch_to schuldhulp_informatiemodel -rt_pkg $ROOT_SCHULDHULP --plugin_class_name DDASPluginInformatiemodel --plugin_file_name ./tools/ddasplugin_informatiemodel.py

# Peform transformation on 'schuldhulp_informatiemodel' and save it to 'schuldhulp_uitwisselmodel'
echo "Extracting and tranforming schuldhulp uitwisselmodel..."
crunch_uml transform -ttp plugin -sch_from schuldhulp_informatiemodel -sch_to schuldhulp_uitwisselmodel -rt_pkg $ROOT_SCHULDHULP --plugin_class_name DDASPluginUitwisselmodel --plugin_file_name ./tools/ddasplugin_uitwisselmodel.py

# Generate JSON Schema from 'schuldhulp_uitwisselmodel'
echo "Generate JSON Schema from uitwisselmodel..."
crunch_uml  -sch schuldhulp_uitwisselmodel export -t json_schema --output_class_id $ROOT_CLASS_UITWISSELMODEL -js_url https://raw.githubusercontent.com/VNG-Realisatie/ddas/main/$version/json_schema_Uitwisselmodel.json -f $JSON

# Generate Markdown for documentation from 'schuldhulp_informatiemodel'
echo "Generate Markdown for documentation if informatiemodel..."
crunch_uml  -sch schuldhulp_informatiemodel export -t jinja2 --output_jinja2_template ddas_markdown.j2 -f $MD --output_jinja2_templatedir ./tools/


# Replace placeholders in uitwisselspecificatie.md.template with version
sed "s/###VERSION###/$version/g" "$UITWISSEL_TEMPLATE" > "$UITWISSEL_MD"

# Generate mkdcos documentation for new version
mkdocs build
# Add new version to documentation tree
mike deploy $version
# Set new version as default
mike set-default $version 
# Deploy documentation
# git push origin gh-pages

# Test