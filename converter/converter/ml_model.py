from transformers import pipeline

# Load a pre-trained model for text generation (this is an example; adjust based on actual use case)
model = pipeline('text-generation', model='gpt-3.5-turbo')

def text_to_html(text):
    result = model(text, max_length=100)[0]['generated_text']
    # Simple conversion to HTML (placeholder logic)
    html_text = result.replace('\n', '<br>')
    return html_text
