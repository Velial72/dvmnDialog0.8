import json
from google.cloud import dialogflow
from environs import Env


def create_intent(project_id, display_name, training_phrases_parts, message_texts):
    """Create an intent of the given intent type."""

    intents_client = dialogflow.IntentsClient()

    parent = dialogflow.AgentsClient.agent_path(project_id)
    training_phrases = []
    for training_phrases_part in training_phrases_parts:
        part = dialogflow.Intent.TrainingPhrase.Part(text=training_phrases_part)
        training_phrase = dialogflow.Intent.TrainingPhrase(parts=[part])
        training_phrases.append(training_phrase)

    text = dialogflow.Intent.Message.Text(text=[message_texts])

    message = dialogflow.Intent.Message(text=text)

    intent = dialogflow.Intent(
        display_name=display_name, training_phrases=training_phrases, messages=[message]
    )

    response = intents_client.create_intent(
        request={"parent": parent, "intent": intent}
    )



def main():
    env = Env()
    env.read_env()
    with open(env('PATH_TO_FILE'), "r", encoding="utf-8") as file:
        questions_json = file.read()
    questions = json.loads(questions_json)

    for theme, question in questions.items():
        some_question = question['questions']
        some_answer = question['answer']
        create_intent(env('DIALOG_ID'), theme, some_question, some_answer)


if __name__ == '__main__':
    main()
