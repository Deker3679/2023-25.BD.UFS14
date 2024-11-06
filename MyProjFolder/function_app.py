import azure.functions as func
import logging
import json

WORDS = {
    "house": "door",
    "dog": "cat",
    "sun": "moon",
    "book": "page",
    "tree": "leaf",
    "car": "wheel",
    "pen": "paper",
    "cup": "coffee"
}

app = func.FunctionApp()

@app.route(route="WordAssociation", auth_level=func.AuthLevel.ANONYMOUS)
def WordAssociation(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    word = req.params.get('word')
    
    if not word:
        return func.HttpResponse(
            json.dumps(WORDS, indent=2),
            mimetype="application/json",
            status_code=200
        )
    
    word = word.lower()
    
    if word in WORDS:
        associated_word = WORDS[word]
        return func.HttpResponse(
            json.dumps({"input": word, "associated": associated_word}),
            mimetype="application/json",
            status_code=200
        )
    else:
        return func.HttpResponse(
            json.dumps({"error": f"No association found for '{word}'"}),
            mimetype="application/json",
            status_code=404
        )