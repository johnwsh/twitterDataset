import os
from openai import OpenAI
import pandas as pd
import base64

def encode_image(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode("utf-8")

def main():

    df = pd.read_csv('captions_limited.csv')
    client = OpenAI()

    for image_path in os.listdir('images'):
        image_path = 'images/' + image_path
        id = image_path[:-4]
        
        if not os.path.exists(image_path):
            print("image not found:", image_path)
            continue
            
        base64_image = encode_image(image_path)

        if id not in df['id'].values:

            response = client.chat.completions.create(
                        model="gpt-4o-mini",
                        messages=[
                            {
                                "role": "user",
                                "content": [
                                    {"type": "text", "text": "Describe this image in details."},
                                    {
                                        "type": "image_url",
                                        "image_url": {
                                            "url": f"data:image/jpeg;base64,{base64_image}",
                                        },
                                    },
                                ],
                            }
                        ],
                        max_tokens=300,
                    )

            caption = response.choices[0].message.content


            df = df._append({'id': id, 'text': caption}, ignore_index=True)
            df.to_csv('captions_limited.csv', index=False)

main()