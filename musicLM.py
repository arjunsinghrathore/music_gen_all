import streamlit as st
import requests

from google.oauth2 import service_account
from googleapiclient.discovery import build
from googleapiclient.http import MediaIoBaseUpload
import io

# Load the Google Drive API credentials
info = {
  "type": "",
  "project_id": "",
  "private_key_id": "",
  "private_key": "",
  "client_email": "",
  "client_id": "",
  "auth_uri": "",
  "token_uri": "",
  "auth_provider_x509_cert_url": "",
  "client_x509_cert_url": "",
  "universe_domain": "googleapis.com"
}
credentials = service_account.Credentials.from_service_account_info(info, scopes=["https://www.googleapis.com/auth/drive"])
drive_service = build('drive', 'v3', credentials=credentials)

def save_file_to_drive(file_data, file_name, mime_type):
    """
    Save the uploaded file to Google Drive.
    """
    file_metadata = {'name': file_name}
    media = MediaIoBaseUpload(io.BytesIO(file_data), mimetype=mime_type)
    file = drive_service.files().create(body=file_metadata, media_body=media, fields='id').execute()
    return file.get('id')

# Streamlit interface setup
st.title("MusicLM")
st.markdown("Upload text, audio, images, or video files for custom music generation.")

# Text input
text_input = st.text_area("Enter your text here")
if st.button('Submit Text', key='submit_text'):
    if text_input:
        # Convert text to bytes and save as .txt
        text_bytes = text_input.encode('utf-8')
        file_id = save_file_to_drive(text_bytes, "input_text.txt", "text/plain")
        st.success(f'Text saved successfully. File ID: {file_id}')
    else:
        st.warning('Please enter some text before submitting.')

# Audio input
audio_file = st.file_uploader("Upload Audio", type=['mp3', 'wav'], key='audio')
if st.button('Submit Audio', key='submit_audio'):
    if audio_file is not None:
        file_id = save_file_to_drive(audio_file.getvalue(), audio_file.name, audio_file.type)
        st.success(f'Audio saved successfully. File ID: {file_id}')
    else:
        st.warning('Please upload an audio file before submitting.')

# Image input
image_file = st.file_uploader("Upload Image", type=['png', 'jpg', 'jpeg'], key='image')
if st.button('Submit Image', key='submit_image'):
    if image_file is not None:
        file_id = save_file_to_drive(image_file.getvalue(), image_file.name, image_file.type)
        st.success(f'Image saved successfully. File ID: {file_id}')
    else:
        st.warning('Please upload an image file before submitting.')

# Video input
video_file = st.file_uploader("Upload Video", type=['mp4', 'mov', 'avi'], key='video')
if st.button('Submit Video', key='submit_video'):
    if video_file is not None:
        file_id = save_file_to_drive(video_file.getvalue(), video_file.name, video_file.type)
        st.success(f'Video saved successfully. File ID: {file_id}')
    else:
        st.warning('Please upload a video file before submitting.')