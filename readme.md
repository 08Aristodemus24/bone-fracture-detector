# This is my first project that will develop a object detection application using opencv, yolo (the latest version), and some GUI libraries like kivy to create a user interface etc.

## Insights:
* useful libraries for extracting text from images include pytesseract. To use pytesseract `pip insatll pytesseract` and define path to tessearact executable in your script that uses pytessereact: `pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe` because when pytesseract is installed it will be installed in our local disk

```
def extract_images_text(pdf):
    """
    works on any pdf file flattened or unflattened by
    extracting any text or image with text within the pdf file
    """
    # define path to tessearact executable
    pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

    # iterate over PDF pages
    data = []
    for page_index, page in enumerate(pdf):

        # get images on the page
        image_list = page.get_images(full=True)

        # if page contains no text then this statement will return 
        # an empty list akin to what page.get_images() naturally returns
        text_list = [] if page.get_text() == "" else page.get_text().split('\n')
        # print(text_list)
        # print(image_list)

        # printing number of images found in this page
        if image_list:
            print(f"[+] Found a total of {len(image_list)} images on page {page_index}")
        else:
            print("[!] No images found on page", page_index)

        data.extend(image_list)
        data.extend(text_list)

    # filter data for any duplicate tuples or whole strings
    data_filt = list(set(data))

    output = []
    for data_index, data in enumerate(data_filt, start=1):

        # note that data may be in a form of a tuple meaning an
        # image or just a full string. If such is the case that it
        # is a tuple proceed with extracting image from pdf and bytes
        # object and read it through pillow then convert to text via 
        # tesseract
        # print(type(data))
        if type(data) == tuple:
            # get the XREF of the image
            xref = data[0]

            # extract the image bytes
            image_obj = pdf.extract_image(xref)
            image_bytes = image_obj["image"]

            # get the image extension
            # image_ext = image_obj["ext"]

            # convert the bytes of the image to BytesIO object
            # so it can be read by Image.open() function
            base_image = Image.open(io.BytesIO(image_bytes))

            # return value will naturally be a giant string with \n char
            # so split it according to \n char to reveal lines
            text = pytesseract.image_to_string(base_image)
            text = text.split('\n')
            output.extend(text)

        elif type(data) == str:
            text = data.split('\n')
            output.extend(text)
    
    return output
```

* most Yolo models e.g. YoloV11 are already pretrained on a general dataset that maybe detects objects like persons, cellphones, combs, laptops, doors, pens, food, etc. When we want to fine tune it how we would a general open source pre trained word embedding model or a language model like llama we would feed it extra data that is our own that we want the model to learn from in this case we want maybe our Yolo model to detect certain writings or sentences on videos or images, which may not be detected by the general model itself, to do this we would have to label our data with the bounding boxes, the width and height of these bounding boxes, the x and y coordinates of the center of the boxes, the one hot encoded representation of the object in the bounding box (if it is a writing or drawing or whatever) then the confidence score or probability of whether an object is present in the image. This is most of the data preprocessing task of just using python code to preprocess our annotated images such that it can be fed as training labels to our model, that we need to fine tune.
* I believe kilangan ko talaga intindihin muna paano pinepreprocess ang dataset for finetuning a Yolo model 
* basically how yolo works on videos is that on the backend it's still using images for its data for object detection. And how it does this is diba yung video is basically multiple frames of images changing and moving to a certain direction. What yolo does is as each frame of the video passes yolo uses this frame as an image and detects lightning quick in real time the objects present in the frame, and then it moves on to the next frame in the video and does the prediction again. 
* Yes, the confidence score in YOLO is essentially a probability. It represents the model's certainty that a detected object is actually present within the bounding box. Think of it as the model saying, "I am X percent sure that there's an object here."
* The confidence score threshold acts as a filter. It determines the minimum level of certainty the model must have for a detection to be considered valid.
* If you set a threshold of 0.1, you're telling the model, "Show me all detections where you're at least 10% sure an object is present."
Therefore, yes, an object with a confidence score of 0.1 or higher would be detected.
* Using a Lower Threshold means more detections will be shown, including those with lower confidence. This increases the risk of false positives (detecting objects that aren't really there). It can be useful when you want to ensure you don't miss any objects, even if it means some incorrect detections.
* And using a Higher Threshold means Fewer detections will be shown, only those with high confidence. This reduces the risk of false positives. It can be useful when you need high accuracy and want to avoid incorrect detections.
* the confidence threshold is a probability value between 0 and 1 that when this is set higher the yolo model detects even the smallest objects in the frame i.e. if a frame of a video has a car from afar but its small that it might as well be ommitted in being detected, Yolo still manages to detect as a car. This is what this threshold value is for

## To do:
### Dataset annotation
* what I want to do is use an open source Yolo model and fine tuen it on my own dataset
* I want to annotate this dataset I have using some kind of open source tool