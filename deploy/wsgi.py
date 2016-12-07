import uwsgi

import json
import subprocess, shlex, os

WEBHOOK_TOKEN = "aa2f8abc7cd94163-8d123c0c880f5494"
WEBROOT = "/root/tianditu"

# params = {
#     "ref": "refs/heads/master",
#     "before": "4ad42825ec241960e58ddd5cb76afd9259d82f6c",
#     "commits": [
#         {
#             "committer":
#                 {
#                     "name": "djskl",
#                     "email": "448189234@qq.com"
#                 },
#              "web_url": "https://coding.net/u/djskl/p/tianditu/git/commit/231140af02f24719c9326a0d2fd367c5fdc16396",
#             "short_message": "\xe6\xb7\xbb\xe5\x8a\xa0\xe9\x83\xa8\xe7\xbd\xb2\xe4\xbb\xa3\xe7\xa0\x81\\n",
#             "sha": "231140af02f24719c9326a0d2fd367c5fdc16396"
#         }
#     ],
#     "after": "231140af02f24719c9326a0d2fd367c5fdc16396",
#     "event": "push",
#     "repository": {
#         "owner": {
#             "path": "/u/djskl",
#             "web_url": "https://coding.net/u/djskl",
#             "global_key": "djskl",
#             "name": "djskl",
#             "avatar": "/static/fruit_avatar/Fruit-19.png"
#         },
#         "https_url": "https://git.coding.net/djskl/tianditu.git",
#         "web_url": "https://coding.net/u/djskl/p/tianditu",
#         "project_id": "623085",
#         "ssh_url": "git@git.coding.net:djskl/tianditu.git",
#         "name": "tianditu",
#         "description": ""
#     },
#     "user": {
#         "path": "/u/djskl",
#         "web_url": "https://coding.net/u/djskl",
#         "global_key": "djskl",
#         "name": "djskl",
#         "avatar": "/static/fruit_avatar/Fruit-19.png"
#     },
#     "token": "aa2f8abc7cd94163-8d123c0c880f5494"
# }


def application(env, start_response):

    try:
        request_body_size = int(env.get('CONTENT_LENGTH', 0))
    except ValueError:
        request_body_size = 0

    params = json.loads(env['wsgi.input'].read(request_body_size))

    token = params.get("token")
    if token != WEBHOOK_TOKEN:
        start_response('400 BAD REQUEST', [('Content-Type', 'text/html')])
        return ""

    _cmd = "sh %s/reset.sh"%WEBROOT
    subprocess.check_call(shlex.split(_cmd))

    for idx in range(8):
        subprocess.Popen(shlex.split("uwsgi --ini uwsgi.ini"), cwd=os.path.join(WEBROOT, "t%s"%(str(idx))))

    start_response('200 OK', [('Content-Type', 'text/html')])
    return "ok"
