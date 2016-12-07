import StringIO
import os, io
import requests
from PIL import Image

TILE_ROOT = "/tdt_tiles"

def getURLS(server_host):
    return {
        "IMG": "http://%s.tianditu.com/DataServer?T=img_w&x={x}&y={y}&l={z}"%server_host,
        "VEC": "http://%s.tianditu.com/DataServer?T=vec_w&x={x}&y={y}&l={z}"%server_host,
        "CIA": "http://%s.tianditu.com/DataServer?T=cia_w&x={x}&y={y}&l={z}"%server_host
    }

def getLocalTile(ttype, x, y, z):
    path = os.path.join(TILE_ROOT, ttype, str(x), str(y))
    tile = os.path.join(path, str(z)+".png")
    if not os.path.exists(tile):
        return None
    return tile

def setLocalTile(img, ttype, x, y, z):
    path = os.path.join(TILE_ROOT, ttype, str(x), str(y))
    if not os.path.exists(path):
        os.makedirs(path)
    tf = os.path.join(path, str(z)+".png")
    img.save(open(tf, "wb"), format='PNG')

def getHttpImg(img):
    imgs = StringIO.StringIO()
    img.save(imgs, format='PNG')
    imgs.seek(0)
    return imgs.getvalue()

def tileCache(func):
    def _wrapper(ttype, x, y, z):
        tf = getLocalTile(ttype, x, y, z)
        if tf and os.path.exists(tf):
            img = Image.open(tf)
            return getHttpImg(img)

        new_img = func(ttype, x, y, z)

        if not new_img:
            return None
        setLocalTile(new_img, ttype, x, y, z)
        return getHttpImg(new_img)
    return _wrapper


class TileApp(object):

    def __init__(self, urls):
        self.urls = urls

    def getTile(self, ttype, x, y, z):
        tf = getLocalTile(ttype, x, y, z)
        if tf and os.path.exists(tf):
            img = Image.open(tf)
            return getHttpImg(img)

        tile_url = self.urls[ttype].format(x=x, y=y, z=z)

        rst = requests.get(tile_url)
        new_img = None
        if rst.status_code == 200:
            cnt = rst.content
            image_file = io.BytesIO(cnt)
            new_img = Image.open(image_file)

        if not new_img:
            return None
        setLocalTile(new_img, ttype, x, y, z)
        return getHttpImg(new_img)

    def __call__(self):

        def _wrapper(env, start_response):
            path_info = env["PATH_INFO"].strip()

            if path_info.startswith("/"):
                path_info = path_info[1:]

            args = path_info.split("/")

            args = args[-4:]
            if len(args) != 4:
                start_response('400 BAD REQUEST', [('Content-Type', 'text/html')])
                return ""

            ttype, x, y, z = args
            ttype = ttype.upper()
            tile_img = self.getTile(ttype, x, y, z)

            start_response('200 OK', [('Content-Type', 'image/png')])
            return [tile_img]

        return _wrapper

if __name__ == "__main__":
    tap = TileApp({
        "IMG": "http://t0.tianditu.com/DataServer?T=img_w&x={x}&y={y}&l={z}",
        "VEC": "http://t0.tianditu.com/DataServer?T=vec_w&x={x}&y={y}&l={z}",
        "CIA": "http://%s.tianditu.com/DataServer?T=cia_w&x={x}&y={y}&l={z}"
    })
    tap.getTile("VEC", 842, 389, 10)