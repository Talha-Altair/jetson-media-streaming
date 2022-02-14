# Jetson Media Streaming

## Running

```
pip install -r requirements.txt
python app.py
```

## Viewing

Open the browser and navigate to: ```http://localhost:6969```

## Testing

Remove or add ```'png', 'jpg', 'jpeg', 'gif'``` files to the ```static/images``` directory.
And then go back to the browser.

## Paramaters

### app.py

- ```IMAGES_DIR```: The directory where the images are stored.
- ```ALLOWED_EXTENSIONS```: The allowed extensions for the images.
- ```PORT```: The port to run the server on.

### index.html

- ```setInterval```: The interval in milliseconds to check for new images.
- ```Title```: The title of the page.

## Customization

The Frontend can be customized by editing the ```index.html``` file with CSS for styling and JS for any new elements if required. 

