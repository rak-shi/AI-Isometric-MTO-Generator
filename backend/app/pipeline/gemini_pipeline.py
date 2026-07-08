import os
import json

from dotenv import load_dotenv
from google import genai

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)

PROMPT = """
You are a senior piping engineer.

Analyze the uploaded piping isometric drawing.

Generate a complete Material Take-Off (MTO).

Return ONLY valid JSON.

The JSON MUST EXACTLY follow this schema.

{
  "drawing_meta": {
    "drawing_no": "",
    "revision": "",
    "line_number": "",
    "nps": "",
    "material_class": "",
    "service": ""
  },

  "items":[
    {
      "item_no":1,
      "category":"PIPE",
      "description":"Pipe Seamless",
      "size_nps":"6\\"",
      "schedule_rating":"SCH40",
      "material_spec":"ASTM A106 Gr.B",
      "end_type":"BW",
      "quantity":1,
      "unit":"M",
      "length_m":12.4,
      "confidence":0.95,
      "remarks":""
    }
  ],

  "summary":{
    "total_pipe_length_m":12.4,
    "fittings":4,
    "flanges":2,
    "valves":1,
    "gaskets":2,
    "bolt_sets":2
  }
}

Rules:

1. Return ONLY JSON.
2. Do NOT return markdown.
3. Do NOT explain.
4. item_no must always exist.
5. category must be one of:
   PIPE
   FITTING
   FLANGE
   VALVE
   GASKET
   BOLT
   SUPPORT
   WELD
6. quantity must always exist.
7. unit must always exist.
8. Unknown values should be "".
9. Never omit any field.
10. Pipe is measured in M.
11. Other components are measured in EA.
12. Return summary totals.
"""


def test_gemini():
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents="Say Gemini Connected Successfully"
    )

    return response.text


def extract_mto(image_path: str):

    uploaded_file = client.files.upload(
        file=image_path
    )

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=[
            uploaded_file,
            PROMPT
        ]
    )

    text = response.text.strip()

    if text.startswith("```"):
        text = (
            text.replace("```json", "")
                .replace("```", "")
                .strip()
        )

    return json.loads(text)