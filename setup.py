
def my_score(teacher_text,students_texts):
      from openai import OpenAI
      OPENAI_API_KEY="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"
      client = OpenAI(
              api_key=OPENAI_API_KEY
        )
      completion = client.chat.completions.create(
          model="gpt-3.5-turbo",
          messages=[
            # {"role": "system", "content": "You are a very strict answer checker, skilled in comparing student answers with teacher answers by matching word by word, compares the number of words to teacher word and give them score in scale of 10, you need to give int score only."},
            {"role": "system", "content": "Use Domain-Specific Models to evaluate student answers with teacher answers and give only score on the scale of 10 giving integer marking only and no other words and be strict"},
              {"role": "user", "content": "teacher answer : "+teacher_text},
            {"role": "user", "content": "student answer : "+students_texts},
          ]
      )
      # print(completion,type(completion))
      return completion.choices[0].message.content