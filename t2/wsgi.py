from tdt import TileApp,getURLS

URLS = getURLS("t2")

tap = TileApp(URLS)

application = tap()