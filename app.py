import gradio as gr
import torch

def transcribe(audio):
    return "Это демо‑версия SeamlessStreaming на CPU. Звук не обрабатывается."

iface = gr.Interface(
    fn=transcribe,
    inputs=gr.Audio(source="microphone", type="filepath"),
    outputs=gr.Textbox(label="📄 Результат"),
    title="SeamlessStreaming CPU Demo",
    description="Простое демо‑приложение на Gradio"
)
iface.launch()
