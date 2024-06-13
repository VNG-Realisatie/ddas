#!/bin/bash

# Controleer of er een argument is opgegeven voor de basisnaam
if [ "$#" -ne 1 ]; then
    echo "Gebruik: echo <inhoud> | $0 <basisnaam_voor_bestanden>"
    exit 1
fi

BASENAME=$1
COUNTER=0
CHUNK_FILE=""

# Lees de invoer van stdin regel voor regel
while IFS= read -r line; do
    # Controleer of de regel begint met een koptekstniveau 1
    if [[ "$line" =~ ^\#\ .+ ]]; then
        # Als er een huidig bestand is, verhoog dan de teller
        if [ ! -z "$CHUNK_FILE" ]; then
            ((COUNTER++))
        fi
        CHUNK_FILE="${BASENAME}_${COUNTER}.md"
        # Maak het nieuwe bestand aan
        > "$CHUNK_FILE"
    fi
    # Als er een huidig bestand is, voeg dan de regel toe
    if [ ! -z "$CHUNK_FILE" ]; then
        echo "$line" >> "$CHUNK_FILE"
    fi
done

echo "De invoer is opgesplitst in $COUNTER + 1 stukken."
