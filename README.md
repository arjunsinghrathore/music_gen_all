# MusicGen-All: Context-Based Music Generation

## Overview
This project presents an end-to-end pipeline for generating music based on various input modalities, including text, audio, and image. At its core, the system utilizes **MusicGen**, a state-of-the-art text-to-music generation model, and enhances its performance using **Retrieval-Augmented Generation (RAG)** to provide context-aware music generation. 

By integrating **context retrieval** from diverse inputs, this project ensures that the generated music aligns with the mood and intent of the user input, improving musical coherence and creativity. 

---

## Features
✅ **Multi-Modal Input Support**: Generate music from text, images, audio, and video inputs.
✅ **Retrieval-Augmented Generation (RAG)**: Context-aware prompts enhance MusicGen outputs.
✅ **Automated Prompt Engineering**: Extracts relevant context for improved generation.
✅ **User-Friendly Interface**: Simple UI to interact and generate music.
✅ **Vector Search for Context Matching**: Finds the most relevant prompts from a pre-trained dataset.

---

## System Architecture
<img width="743" alt="image" src="https://github.com/user-attachments/assets/c4c9d49f-009a-4eee-b00d-e4fd34803a5e" />


1. **User Input Processing**:
   - Text inputs are directly processed.
   - Images are analyzed using `GPT-4-Vision` to generate captions.
   - Audio inputs are transcribed into text via `Whisper API`.
   - Video inputs undergo caption extraction using `Vid2Seq`.

2. **Context Generation via RAG**:
   - Extracts keywords from input using `GPT`.
   - Searches for relevant musical prompts in a vector database.
   - Generates refined prompts for `MusicGen` using the most relevant contextual information.

3. **Music Generation with MusicGen API**:
   - Generated prompts are fed into `MusicGen`.
   - Outputs high-quality, contextually relevant music.

---

## Installation & Setup
```bash
git clone https://github.com/arjunsinghrathore/music_gen_all.git
cd music_gen_all
pip install -r requirements.txt
```
Ensure you have access to APIs for:
- **OpenAI GPT (for context extraction & keyword retrieval)**
- **Facebook MusicGen (for music generation)**
- **Whisper API (for audio-to-text transcription)**

---

## Usage
Run the pipeline:
```bash
python main.py --input_type text --input "A relaxing jazz melody for a quiet evening."
```
For an image input:
```bash
python main.py --input_type image --input "path/to/image.jpg"
```
For video/audio inputs, specify file paths and the system will extract context accordingly.

---

## Example Outputs
🎵 **Generated Music Sample**: [Listen here](https://github.com/arjunsinghrathore/music_gen_all/samples/output.mp3)

---

## Technologies Used
- **MusicGen** (Meta AI) - Text-to-Music generation
- **GPT-4 & Whisper** (OpenAI) - Context extraction & processing
- **Vid2Seq** - Video captioning
- **Vector Search & Embeddings** - Context retrieval & similarity matching
- **Flask/Dash UI** (optional) - User-friendly interface

---

## Future Enhancements
🔹 Improve vector database for more accurate retrieval.
🔹 Integrate fine-tuning mechanisms for MusicGen.
🔹 Expand UI with more customization options.

---

## Contributors
👤 **Arjun Singh Rathore** 
👤 **Shriyesh Chandra**
👤 **Tanmay G Dhadhania**  
👤 **Rahi Krishna**  


---

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## Acknowledgments
🙏 Thanks to **Meta AI** for MusicGen and **OpenAI** for their APIs.
