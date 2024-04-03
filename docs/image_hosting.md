Dự án sử dụng hosting của ImgBB

# Image Upload
```
https://api.imgbb.com/1/upload
```

Parameters
- key (required)
`The API key.`

- image (required)
`A binary file, base64 data, or a URL for an image. (up to 32 MB)`

- name (optional)
`The name of the file, this is automatically detected if uploading a file with a POST and multipart / form-data`

- expiration (optional)
`Enable this if you want to force uploads to be auto deleted after certain time (in seconds 60-15552000)`

# Request method
API v1 calls can be done using the POST or GET request methods but since GET request are limited by the maximum allowed length of an URL you should prefer the POST request method.

# Example response (JSON)
```Json
{
  "data": {
    "id": "2ndCYJK",
    "title": "c1f64245afb2",
    "url_viewer": "https://ibb.co/2ndCYJK",
    "url": "https://i.ibb.co/w04Prt6/c1f64245afb2.gif",
    "display_url": "https://i.ibb.co/98W13PY/c1f64245afb2.gif",
    "width":"1",
    "height":"1",
    "size": "42",
    "time": "1552042565",
    "expiration":"0",
    "image": {
      "filename": "c1f64245afb2.gif",
      "name": "c1f64245afb2",
      "mime": "image/gif",
      "extension": "gif",
      "url": "https://i.ibb.co/w04Prt6/c1f64245afb2.gif",
    },
    "thumb": {
      "filename": "c1f64245afb2.gif",
      "name": "c1f64245afb2",
      "mime": "image/gif",
      "extension": "gif",
      "url": "https://i.ibb.co/2ndCYJK/c1f64245afb2.gif",
    },
    "medium": {
      "filename": "c1f64245afb2.gif",
      "name": "c1f64245afb2",
      "mime": "image/gif",
      "extension": "gif",
      "url": "https://i.ibb.co/98W13PY/c1f64245afb2.gif",
    },
    "delete_url": "https://ibb.co/2ndCYJK/670a7e48ddcb85ac340c717a41047e5c"
  },
  "success": true,
  "status": 200
}
```
