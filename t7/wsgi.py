from tdt import TileApp, getURLS

URLS = getURLS("t7")

tap = TileApp(URLS)

application = tap()