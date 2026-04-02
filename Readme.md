# 🔍 AI Image Identifier
- This is the project which identifies and then predicts of the uploaded image and this uses the pretrained ML Model data from mobilenetv2 which is the tensorflow library and if you have genai api key code you can get the accurate prediction of that image for identifying the data.

- By default, the model can identify 1,000 distinct object categories. These include a broad variety of "everyday" web images rather than           specific people or niche professional data.

  - Link show all the 1000 object categories of my project - https://www.kaggle.com/datasets/skyap79/imagenet-classes


- Accuracy Details of this project 
- MobileNetV2 (Standard): This model, pre-trained on ImageNet, typically has around 71.3% top-1 accuracy. This means it correctly identifies the    primary object about 71% of the time. Its top-5 accuracy is around 90.1%.
- Gemini 1.5 Flash: As a large multimodal model, Gemini can achieve above 90% accuracy in many situations because it understands context and        details that smaller models may miss. 
- Methods to Increase Accuracy
- To reach 90% accuracy,consider these options:
- Use Gemini: The Gemini API can be used as the primary identification source. It is more accurate for complex images.
- Fine-tune MobileNetV2: Transfer Learning can be performed by training the model on a smaller, high-quality dataset. For a specific task, this     can lead to 92% to 98% accuracy.
- Improve Image Quality: AI accuracy can be affected by poor image quality. Clear, centered images can improve performance. 

- Comparison
 --------------------------------------------------------------------------------------------------
- | Features  	           |  MobileNetV2 (Default)          |	      Gemini 1.5 Flash              |
- | Top-1                  |   Accuracy	~71%	               |     >90% (Context dependent)         |
- | Best Use Case	         |  Fast, local object naming      |	  Detailed reasoning & celebrity ID | 
- | Internet Required      |	  No	                         |            Yes                       |
- | Reasoning Ability	     |   None (Math only)              |	       High (Human-like)            |
 --------------------------------------------------------------------------------------------------


Code Explanation
- google.generativeai: (this require an api key to use this model) This is to prepare the app for future Gemini integration.
- numpy: This is the python library that handles image data as a numerical array.
- streamlit: The framework builds the web interface to run project in default host webpage.
- MobileNetV2: This is a pre-trained deep learning model from TensorFlow.
- PIL (Image): It opens and changes uploaded image files.
- @st.cache_resource: This Streamlit decorator loads the model into memory only once. This is important because the model is 14MB. Without this,    the app loading time will be slow.
- image.convert("RGB"): This makes sure the image has 3 color channels (Red, Green, Blue).
- resize((224,224)): MobileNetV2 was trained on images of this size.
- preprocess_input: This adjusts the pixel values to match the original training data.
- np.expand_dims: This adds a "batch" dimension. The model needs a list of images, so this turns the single image into a list of one.
- model.predict: This analyzes the pixels and returns 1,000 probabilities.
- decode_predictions: This turns the numbers into labels like "Labrador".
- top=1: This makes the app only return the most likely result and only one output.
- set_page_config: This sets the title that appears in the browser tab.
- st.markdown**: This adds Custom CSS to change the background color, button style, and font colors for a professional look.
- file_uploader**: This creates the drag-and-drop zone for uploading the file.
- st.button: This starts the AI calculation when the user is ready.
- st.spinner: This shows a loading animation while photo is identifying.
- st.progress: This turns the decimal score into a visual blue bar.
- {score:.2%}: This formats the number as a percentage with two decimal places. for example ( 0.25)





## ✨ Features
- **Instant Classification**: Identify 1,000+ different object categories (animals, vehicles, household items, etc.).
- **Confidence Visualization**: Real-time progress bars showing the model's match probability.
- **Modern UI**: Custom CSS styling with a responsive, centered layout.
- **Resource Caching**: Uses `@st.cache_resource` to load the 14mb  model file once, ensuring fast performance for subsequent uses.

## 🚀 How to Run  This Repository Locally

### Prerequisites
- Python 3.9 or higher
- My suggestion is that you create separate env
- type python -m venv (your_desired_name) # IN Terminal
- To activate if not activated you press  
- yur_desired_name\scripts\Activate.ps1 # (Here ps1 IS FOR POWERSHELL)
- Pip (Python package manager)
- To run in your computer you should use type the following codes in terminal
- pip install google-generativeai
- pip install streamlit tensorflow numpy pillow
-  After downloading use command in terminal
-  streamlit run app.py

### Installation
1. **Clone the repository:**
   ```bash
   git clone https://github.com
   cd AI-Image-Identifier
