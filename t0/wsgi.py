from tdt import TileApp, getURLS

URLS = getURLS("t0")

tap = TileApp(URLS)

application = tap()