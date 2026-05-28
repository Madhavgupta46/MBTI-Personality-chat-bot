{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": []
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "code",
      "source": [
        "!pip install streamlit"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "0YW9jc_0vOHm",
        "outputId": "59ac8a31-6cff-4cda-a21c-8de6f7ec1013"
      },
      "execution_count": 15,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Collecting streamlit\n",
            "  Downloading streamlit-1.57.0-py3-none-any.whl.metadata (9.6 kB)\n",
            "Requirement already satisfied: altair!=5.4.0,!=5.4.1,<7,>=4.0 in /usr/local/lib/python3.12/dist-packages (from streamlit) (5.5.0)\n",
            "Requirement already satisfied: blinker<2,>=1.5.0 in /usr/local/lib/python3.12/dist-packages (from streamlit) (1.9.0)\n",
            "Requirement already satisfied: cachetools<8,>=5.5 in /usr/local/lib/python3.12/dist-packages (from streamlit) (6.2.6)\n",
            "Requirement already satisfied: click<9,>=7.0 in /usr/local/lib/python3.12/dist-packages (from streamlit) (8.4.0)\n",
            "Requirement already satisfied: gitpython!=3.1.19,<4,>=3.0.7 in /usr/local/lib/python3.12/dist-packages (from streamlit) (3.1.50)\n",
            "Requirement already satisfied: numpy<3,>=1.23 in /usr/local/lib/python3.12/dist-packages (from streamlit) (2.0.2)\n",
            "Requirement already satisfied: packaging>=20 in /usr/local/lib/python3.12/dist-packages (from streamlit) (26.2)\n",
            "Requirement already satisfied: pandas<4,>=1.4.0 in /usr/local/lib/python3.12/dist-packages (from streamlit) (2.2.2)\n",
            "Requirement already satisfied: pillow<13,>=7.1.0 in /usr/local/lib/python3.12/dist-packages (from streamlit) (11.3.0)\n",
            "Collecting pydeck<1,>=0.8.0b4 (from streamlit)\n",
            "  Downloading pydeck-0.9.2-py2.py3-none-any.whl.metadata (4.2 kB)\n",
            "Requirement already satisfied: protobuf<8,>=3.20 in /usr/local/lib/python3.12/dist-packages (from streamlit) (5.29.6)\n",
            "Requirement already satisfied: pyarrow>=7.0 in /usr/local/lib/python3.12/dist-packages (from streamlit) (18.1.0)\n",
            "Requirement already satisfied: requests<3,>=2.27 in /usr/local/lib/python3.12/dist-packages (from streamlit) (2.32.4)\n",
            "Requirement already satisfied: tenacity<10,>=8.1.0 in /usr/local/lib/python3.12/dist-packages (from streamlit) (9.1.4)\n",
            "Requirement already satisfied: toml<2,>=0.10.1 in /usr/local/lib/python3.12/dist-packages (from streamlit) (0.10.2)\n",
            "Requirement already satisfied: typing-extensions<5,>=4.10.0 in /usr/local/lib/python3.12/dist-packages (from streamlit) (4.15.0)\n",
            "Requirement already satisfied: starlette>=0.40.0 in /usr/local/lib/python3.12/dist-packages (from streamlit) (0.52.1)\n",
            "Requirement already satisfied: uvicorn>=0.30.0 in /usr/local/lib/python3.12/dist-packages (from streamlit) (0.47.0)\n",
            "Requirement already satisfied: httptools>=0.6.3 in /usr/local/lib/python3.12/dist-packages (from streamlit) (0.7.1)\n",
            "Requirement already satisfied: anyio>=4.0.0 in /usr/local/lib/python3.12/dist-packages (from streamlit) (4.13.0)\n",
            "Requirement already satisfied: python-multipart>=0.0.10 in /usr/local/lib/python3.12/dist-packages (from streamlit) (0.0.29)\n",
            "Requirement already satisfied: websockets>=12.0.0 in /usr/local/lib/python3.12/dist-packages (from streamlit) (15.0.1)\n",
            "Requirement already satisfied: itsdangerous>=2.1.2 in /usr/local/lib/python3.12/dist-packages (from streamlit) (2.2.0)\n",
            "Requirement already satisfied: watchdog<7,>=2.1.5 in /usr/local/lib/python3.12/dist-packages (from streamlit) (6.0.0)\n",
            "Requirement already satisfied: jinja2 in /usr/local/lib/python3.12/dist-packages (from altair!=5.4.0,!=5.4.1,<7,>=4.0->streamlit) (3.1.6)\n",
            "Requirement already satisfied: jsonschema>=3.0 in /usr/local/lib/python3.12/dist-packages (from altair!=5.4.0,!=5.4.1,<7,>=4.0->streamlit) (4.26.0)\n",
            "Requirement already satisfied: narwhals>=1.14.2 in /usr/local/lib/python3.12/dist-packages (from altair!=5.4.0,!=5.4.1,<7,>=4.0->streamlit) (2.21.2)\n",
            "Requirement already satisfied: idna>=2.8 in /usr/local/lib/python3.12/dist-packages (from anyio>=4.0.0->streamlit) (3.15)\n",
            "Requirement already satisfied: gitdb<5,>=4.0.1 in /usr/local/lib/python3.12/dist-packages (from gitpython!=3.1.19,<4,>=3.0.7->streamlit) (4.0.12)\n",
            "Requirement already satisfied: python-dateutil>=2.8.2 in /usr/local/lib/python3.12/dist-packages (from pandas<4,>=1.4.0->streamlit) (2.9.0.post0)\n",
            "Requirement already satisfied: pytz>=2020.1 in /usr/local/lib/python3.12/dist-packages (from pandas<4,>=1.4.0->streamlit) (2025.2)\n",
            "Requirement already satisfied: tzdata>=2022.7 in /usr/local/lib/python3.12/dist-packages (from pandas<4,>=1.4.0->streamlit) (2026.2)\n",
            "Requirement already satisfied: charset_normalizer<4,>=2 in /usr/local/lib/python3.12/dist-packages (from requests<3,>=2.27->streamlit) (3.4.7)\n",
            "Requirement already satisfied: urllib3<3,>=1.21.1 in /usr/local/lib/python3.12/dist-packages (from requests<3,>=2.27->streamlit) (2.5.0)\n",
            "Requirement already satisfied: certifi>=2017.4.17 in /usr/local/lib/python3.12/dist-packages (from requests<3,>=2.27->streamlit) (2026.5.20)\n",
            "Requirement already satisfied: h11>=0.8 in /usr/local/lib/python3.12/dist-packages (from uvicorn>=0.30.0->streamlit) (0.16.0)\n",
            "Requirement already satisfied: smmap<6,>=3.0.1 in /usr/local/lib/python3.12/dist-packages (from gitdb<5,>=4.0.1->gitpython!=3.1.19,<4,>=3.0.7->streamlit) (5.0.3)\n",
            "Requirement already satisfied: MarkupSafe>=2.0 in /usr/local/lib/python3.12/dist-packages (from jinja2->altair!=5.4.0,!=5.4.1,<7,>=4.0->streamlit) (3.0.3)\n",
            "Requirement already satisfied: attrs>=22.2.0 in /usr/local/lib/python3.12/dist-packages (from jsonschema>=3.0->altair!=5.4.0,!=5.4.1,<7,>=4.0->streamlit) (26.1.0)\n",
            "Requirement already satisfied: jsonschema-specifications>=2023.03.6 in /usr/local/lib/python3.12/dist-packages (from jsonschema>=3.0->altair!=5.4.0,!=5.4.1,<7,>=4.0->streamlit) (2025.9.1)\n",
            "Requirement already satisfied: referencing>=0.28.4 in /usr/local/lib/python3.12/dist-packages (from jsonschema>=3.0->altair!=5.4.0,!=5.4.1,<7,>=4.0->streamlit) (0.37.0)\n",
            "Requirement already satisfied: rpds-py>=0.25.0 in /usr/local/lib/python3.12/dist-packages (from jsonschema>=3.0->altair!=5.4.0,!=5.4.1,<7,>=4.0->streamlit) (0.30.0)\n",
            "Requirement already satisfied: six>=1.5 in /usr/local/lib/python3.12/dist-packages (from python-dateutil>=2.8.2->pandas<4,>=1.4.0->streamlit) (1.17.0)\n",
            "Downloading streamlit-1.57.0-py3-none-any.whl (9.2 MB)\n",
            "\u001b[2K   \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m9.2/9.2 MB\u001b[0m \u001b[31m50.2 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25hDownloading pydeck-0.9.2-py2.py3-none-any.whl (11.3 MB)\n",
            "\u001b[2K   \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m11.3/11.3 MB\u001b[0m \u001b[31m75.6 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25hInstalling collected packages: pydeck, streamlit\n",
            "Successfully installed pydeck-0.9.2 streamlit-1.57.0\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "import streamlit as st"
      ],
      "metadata": {
        "id": "Qdbai7_ZvRFK"
      },
      "execution_count": 16,
      "outputs": []
    },
    {
      "cell_type": "code",
      "execution_count": 1,
      "metadata": {
        "id": "vx2nXJpc6zko"
      },
      "outputs": [],
      "source": [
        "import re\n",
        "import pickle\n",
        "\n",
        "from tensorflow.keras.models import load_model\n",
        "from tensorflow.keras.preprocessing.sequence import pad_sequences"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "st.title(\"AI MBTI Personality Chatbot\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "4_r8PXTCvUAn",
        "outputId": "798b12dc-857c-4fa1-d769-e4b8f3a272b0"
      },
      "execution_count": 17,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stderr",
          "text": [
            "2026-05-28 13:19:17.394 WARNING streamlit.runtime.scriptrunner_utils.script_run_context: Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2026-05-28 13:19:18.493 \n",
            "  \u001b[33m\u001b[1mWarning:\u001b[0m to view this Streamlit app on a browser, run it with the following\n",
            "  command:\n",
            "\n",
            "    streamlit run /usr/local/lib/python3.12/dist-packages/colab_kernel_launcher.py [ARGUMENTS]\n",
            "2026-05-28 13:19:18.495 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2026-05-28 13:19:18.497 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n"
          ]
        },
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "DeltaGenerator()"
            ]
          },
          "metadata": {},
          "execution_count": 17
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "IE_model = load_model(\"IE_model.h5\")\n",
        "\n",
        "NS_model = load_model(\"NS_model.h5\")\n",
        "\n",
        "TF_model = load_model(\"TF_model.h5\")\n",
        "\n",
        "JP_model = load_model(\"JP_model.h5\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "4ERt2g537evW",
        "outputId": "2cc73f3c-e44c-4f4c-deb4-727e555444d5"
      },
      "execution_count": 2,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stderr",
          "text": [
            "WARNING:absl:Compiled the loaded model, but the compiled metrics have yet to be built. `model.compile_metrics` will be empty until you train or evaluate the model.\n",
            "WARNING:absl:Compiled the loaded model, but the compiled metrics have yet to be built. `model.compile_metrics` will be empty until you train or evaluate the model.\n",
            "WARNING:absl:Compiled the loaded model, but the compiled metrics have yet to be built. `model.compile_metrics` will be empty until you train or evaluate the model.\n",
            "WARNING:absl:Compiled the loaded model, but the compiled metrics have yet to be built. `model.compile_metrics` will be empty until you train or evaluate the model.\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "with open('tokenizer.pkl', 'rb') as f:\n",
        "    tokenizer = pickle.load(f)"
      ],
      "metadata": {
        "id": "BUZXYa1j73kh"
      },
      "execution_count": 3,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "max_len = 200"
      ],
      "metadata": {
        "id": "v5nuVqp-76bc"
      },
      "execution_count": 4,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "def clean_text(text):\n",
        "\n",
        "    text = text.lower()\n",
        "\n",
        "    text = re.sub(r'http\\S+', '', text)\n",
        "\n",
        "    text = re.sub(r'[^a-zA-Z\\s]', ' ', text)\n",
        "\n",
        "    text = re.sub(r'\\s+', ' ', text).strip()\n",
        "\n",
        "    return text"
      ],
      "metadata": {
        "id": "-uuMDxIP79tQ"
      },
      "execution_count": 5,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "def predict_mbti(text):\n",
        "\n",
        "    # clean text\n",
        "    text = clean_text(text)\n",
        "\n",
        "    # convert text to sequence\n",
        "    seq = tokenizer.texts_to_sequences([text])\n",
        "\n",
        "    # pad sequence\n",
        "    padded = pad_sequences(\n",
        "        seq,\n",
        "        maxlen=max_len,\n",
        "        padding='post',\n",
        "        truncating='post'\n",
        "    )\n",
        "\n",
        "    # predictions\n",
        "    IE_pred = IE_model.predict(padded)[0][0]\n",
        "\n",
        "    NS_pred = NS_model.predict(padded)[0][0]\n",
        "\n",
        "    TF_pred = TF_model.predict(padded)[0][0]\n",
        "\n",
        "    JP_pred = JP_model.predict(padded)[0][0]\n",
        "\n",
        "    # probabilities to letters\n",
        "    ie = 'E' if IE_pred >= 0.1 else 'I'\n",
        "\n",
        "    ns = 'S' if NS_pred >= 0.1 else 'N'\n",
        "\n",
        "    tf = 'F' if TF_pred >= 0.1 else 'T'\n",
        "\n",
        "    jp = 'P' if JP_pred >= 0.1 else 'J'\n",
        "\n",
        "    # final mbti\n",
        "    mbti = ie + ns + tf + jp\n",
        "\n",
        "    return mbti"
      ],
      "metadata": {
        "id": "z4-9RZVg7--E"
      },
      "execution_count": 6,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "questions = [\n",
        "\n",
        "    \"How do you usually spend your weekends?\",\n",
        "\n",
        "    \"What kind of social situations make you comfortable?\",\n",
        "\n",
        "    \"How do you make important decisions?\",\n",
        "\n",
        "    \"Do you prefer planning things or being spontaneous?\",\n",
        "\n",
        "    \"How do you react after a stressful day?\",\n",
        "\n",
        "    \"Would you rather work alone or in a team?\",\n",
        "\n",
        "    \"Do you enjoy practical work or theoretical ideas more?\",\n",
        "\n",
        "    \"How do you prepare before important events?\",\n",
        "\n",
        "    \"What type of conversations do you enjoy the most?\",\n",
        "\n",
        "    \"What motivates you the most in life?\"\n",
        "]"
      ],
      "metadata": {
        "id": "qjySpAKA8Bu5"
      },
      "execution_count": 7,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "responses = []"
      ],
      "metadata": {
        "id": "Ixu7XNoR8FBf"
      },
      "execution_count": 8,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "print(\"===== MBTI Personality Chatbot =====\\n\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "vWZSbMPg8Gfg",
        "outputId": "83719d60-fe74-4cf5-f053-770807203f52"
      },
      "execution_count": 9,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "===== MBTI Personality Chatbot =====\n",
            "\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "for q in questions:\n",
        "\n",
        "    ans = input(q + \"\\n\\nYou: \")\n",
        "\n",
        "    responses.append(ans)\n",
        "\n",
        "    print()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "FKIchSDL8H5n",
        "outputId": "6d1c670d-7f45-4fa9-d528-ec141b18c91b"
      },
      "execution_count": 10,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "How do you usually spend your weekends?\n",
            "\n",
            "You: \n",
            "\n",
            "What kind of social situations make you comfortable?\n",
            "\n",
            "You: skip\n",
            "\n",
            "How do you make important decisions?\n",
            "\n",
            "You: skip\n",
            "\n",
            "Do you prefer planning things or being spontaneous?\n",
            "\n",
            "You: kip\n",
            "\n",
            "How do you react after a stressful day?\n",
            "\n",
            "You: lki\n",
            "\n",
            "Would you rather work alone or in a team?\n",
            "\n",
            "You: ss\n",
            "\n",
            "Do you enjoy practical work or theoretical ideas more?\n",
            "\n",
            "You: s\n",
            "\n",
            "How do you prepare before important events?\n",
            "\n",
            "You: s\n",
            "\n",
            "What type of conversations do you enjoy the most?\n",
            "\n",
            "You: s\n",
            "\n",
            "What motivates you the most in life?\n",
            "\n",
            "You: s\n",
            "\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "full_text = \" \".join(responses)"
      ],
      "metadata": {
        "id": "_4exEyJT8J8R"
      },
      "execution_count": 11,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "result = predict_mbti(full_text)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "ZSCWKGKV9AXB",
        "outputId": "e1f2d519-c608-476c-b145-1dae12932935"
      },
      "execution_count": 12,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "\u001b[1m1/1\u001b[0m \u001b[32m━━━━━━━━━━━━━━━━━━━━\u001b[0m\u001b[37m\u001b[0m \u001b[1m1s\u001b[0m 834ms/step\n",
            "\u001b[1m1/1\u001b[0m \u001b[32m━━━━━━━━━━━━━━━━━━━━\u001b[0m\u001b[37m\u001b[0m \u001b[1m0s\u001b[0m 429ms/step\n",
            "\u001b[1m1/1\u001b[0m \u001b[32m━━━━━━━━━━━━━━━━━━━━\u001b[0m\u001b[37m\u001b[0m \u001b[1m1s\u001b[0m 506ms/step\n",
            "\u001b[1m1/1\u001b[0m \u001b[32m━━━━━━━━━━━━━━━━━━━━\u001b[0m\u001b[37m\u001b[0m \u001b[1m1s\u001b[0m 651ms/step\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "print(\"\\n===== FINAL PERSONALITY RESULT =====\")\n",
        "\n",
        "print(\"\\nPredicted MBTI Type:\", result)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "hAYEnNNX9CIT",
        "outputId": "748d07f1-bea2-4d62-912d-0964e5271de8"
      },
      "execution_count": 13,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "\n",
            "===== FINAL PERSONALITY RESULT =====\n",
            "\n",
            "Predicted MBTI Type: INFP\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [],
      "metadata": {
        "id": "WnYxCT6RvdL4"
      },
      "execution_count": null,
      "outputs": []
    }
  ]
}
