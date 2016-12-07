from tdt import TileApp, getURLS

URLS = getURLS("t3")

tap = TileApp(URLS)

application = tap()