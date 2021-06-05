# Speech2Image

Speech2Image is a image search tool by speech. The application make use of Convolutional Neural Network (CNN) with Mel-frequency cepstral coefficients(MFCC) features

## Installation

Install and run the application:

```bash
cd backend
pip install -r requirement.txt
uvicorn main:app --reload
cd ../frontend
pip install npm
npm install
npm start
```

## Usage

There are 2 ways you can use the application:
- Use record speech funtion
- Upload a speech audio file

The application will classify and display images correspond to your audio input.

Currently the application can classify 4 word: căn hộ, học sinh, người, cảnh sát.

