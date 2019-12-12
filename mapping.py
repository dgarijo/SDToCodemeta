import requests
from pyld import jsonld
import json

modelId = "TOPOFLOW"
r = requests.get(
    #'https://query.mint.isi.edu/api/dgarijo/MINT-ModelCatalogQueries/getResourceMetadata?mv=https%3A%2F%2Fw3id.org%2Fokn%2Fi%2Fmint%2FTOPOFLOW&endpoint=http%3A%2F%2Fontosoft.isi.edu%3A3030%2FmodelCatalog-1.1.0%2Fquery',
    #params={'q': 'requests+language:python'},
    'https://api.models.mint.isi.edu/v1.1.0/models/'+modelId+'?username=mint%40isi.edu',
    headers={'Accept': 'application/json'},
)
#print(r.content)
response = json.loads(r.content.decode('utf-8'))
print(response)
#response['results']['bindings']['prop']['value']['description']


conversion = {}
conversion['@context']='https://doi.org/10.5063/schema/codemeta-2.0'
#Should use the dictionary by Tom.
#OKG-Soft -> Codemeta
mapping={'description':'description', 'keywords':'keywords','hasDownloadURL':'downloadUrl',
         'codeRepository':'codeRepository','applicationCategory':'hasModelCategory','memoryRequirements':'memoryRequirements',
         'operatingSystem':'operatingSystem','processorRequirements':'processorRequirements','softwareRequirements':'softwareRequirements',
         'hasVersionId':'hasVersionId','author':'author','citation':'citation','contributor':'contributor','copyrightHolder':'copyrightHolder',
         'copyrightYear':'copyrightYear','dateCreated':'dateCreated','dateModified':'dateModified','datePublished':'datePublished',
         'funder':'fundingSource','license':'license','publisher':'publisher','version':'hasVersionId','identifier':'identifier',
         'name':'label','funding':'fundingSource','referencePublication':'referencePublication'}

for prop in response:#prop has OKG-Soft vocabulary
    if prop in mapping:
        codemetaMapping = mapping[prop]
        conversion[codemetaMapping] = response[prop]
    #exceptions
    # the following below doesn't work
    #if prop in "hasSourceCode":
    #    conversion["targetProduct"] = response[prop]

print(json.dumps(conversion))
#print the expanded version if needed
#print(jsonld.expand(conversion))
