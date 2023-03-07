# Note: you need to be using OpenAI Python v0.27.0 for the code below to work
import openai
openai.api_key = 'enter-your-api-key'
audio_file= open("./sample.mp3", "rb")
transcript = openai.Audio.transcribe("whisper-1", audio_file)
print(transcript)

# output1 when file is sample.mp3
#{
#   "text": "My thought I have nobody by a beauty and will as you've poured. Mr. Rochester is sub, and that so don't find simpest, And devoted abode, to had my'd in a row,"
# }


# output2 when the file is genevieve.wav
# {
# "text": "This dynamic workshop aims to provide up-to-date information on pharmacological approaches, issues, and treatment in the geriatric population to assist in preventing medication-related problems, appropriately and effectively managing medications and compliance. The concept of polypharmacy, taking multiple types of drugs, will also be discussed, as this is a common issue that can impact adverse side effects in the geriatric population. Participants will leave with the knowledge and considerations of common drug interaction and how to minimize effects that limit function. Summit Professional Education is approved provider of continuing education. This course is offered for six units. This course contains content classified under both the domain of occupational therapy and professional issues, period."
#}
