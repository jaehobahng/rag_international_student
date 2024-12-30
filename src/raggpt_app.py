import gradio as gr
from utils.upload_file import UploadFile
from utils.chatbot import ChatBot
from utils.ui_settings import UISettings

with gr.Blocks() as demo:
    with gr.Tabs():
        with gr.TabItem("RAG-GPT"):
            ##############
            # First ROW:
            ##############
            with gr.Row() as row_one:
                with gr.Column(visible=False) as reference_bar:
                    ref_output = gr.Markdown(height=500)

                with gr.Column() as chatbot_output:
                    chatbot = gr.Chatbot(
                        [],
                        elem_id="chatbot",
                        bubble_full_width=False,
                        height=500,
                        avatar_images=(
                            ("images/thinking.png"), "images/openai_.png"),
                    )
                    chatbot.like(UISettings.feedback, None, None)
            ##############
            # SECOND ROW:
            ##############
            with gr.Row():
                input_txt = gr.Textbox(
                    lines=1,
                    scale=8,
                    placeholder="Enter text and press enter, or upload PDF files",
                    container=False,
                )

            ##############
            # Third ROW:
            ##############
            with gr.Row() as row_two:
                text_submit_btn = gr.Button(value="Submit text")
                sidebar_state = gr.State(False)
                btn_toggle_sidebar = gr.Button(
                    value="References")
                btn_toggle_sidebar.click(UISettings.toggle_sidebar, [sidebar_state], [
                    reference_bar, sidebar_state])
                upload_btn = gr.UploadButton(
                    "📁 Upload PDF or doc files", file_types=[
                        '.pdf',
                        '.doc'
                    ],
                    file_count="multiple")
                temperature_bar = gr.Slider(minimum=0, maximum=1, value=0, step=0.1,
                                            label="Temperature", info="Choose between 0 and 1")
                rag_with_dropdown = gr.Dropdown(
                    label="RAG with", choices=["Preprocessed doc", "Upload doc: Process for RAG"], value="Preprocessed doc")
                clear_button = gr.ClearButton([input_txt, chatbot])

            ##############
            # Process:
            ##############
            # Bind the Enter key to the Submit button action
            input_txt.submit(
                fn=ChatBot.respond,
                inputs=[chatbot, input_txt, rag_with_dropdown, temperature_bar],
                outputs=[input_txt, chatbot, ref_output]
            )

            # Also allow the Submit button to be clicked manually
            text_submit_btn.click(
                fn=ChatBot.respond,
                inputs=[chatbot, input_txt, rag_with_dropdown, temperature_bar],
                outputs=[input_txt, chatbot, ref_output]
            )

            # Ensure pressing Enter triggers the same action as clicking the Submit button
            input_txt.submit(
                fn=lambda *args: text_submit_btn.click(),
                inputs=[],
                outputs=[]
            )

            upload_btn.upload(
                fn=UploadFile.process_uploaded_files,
                inputs=[upload_btn, chatbot, rag_with_dropdown],
                outputs=[input_txt, chatbot],
                queue=False,
            )



if __name__ == "__main__":
    demo.launch(server_name="0.0.0.0", server_port=8001)