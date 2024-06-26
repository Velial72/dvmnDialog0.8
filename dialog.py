from google.cloud import dialogflow


def detect_intent_text(project_id, session_id, message_to_dialogflow, language_code='ru'):
    session_client = dialogflow.SessionsClient()
    session = session_client.session_path(project_id, session_id)

    text_input = dialogflow.TextInput(text=message_to_dialogflow, language_code=language_code)
    query_input = dialogflow.QueryInput(text=text_input)
    response = session_client.detect_intent(
        request={"session": session, "query_input": query_input}
    )
    serialized_answer = {
        'intention': response.query_result.intent.display_name,
        'confidence': response.query_result.intent_detection_confidence,
        'answer': response.query_result.fulfillment_text,
        'fallback': response.query_result.intent.is_fallback
    }

    return serialized_answer
