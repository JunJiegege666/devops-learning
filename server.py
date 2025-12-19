from http.server import BaseHTTPRequestHandler, HTTPServer
import redis
import socket

# 连接 Redis
# ⚠️ 关键点：host 不是 '127.0.0.1'，而是 'redis' (这是我们在 docker-compose 里给服务起的名字)
r = redis.Redis(host='redis', port=6379, db=0)

class SimpleHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        try:
            # 访问 Redis，让计数器 +1
            count = r.incr('hits')
            # 获取当前容器的主机名 (看看是哪个副本在处理请求)
            hostname = socket.gethostname()

            message = f"🎉 Success! DevOps Pipeline is working perfectly!\n(Processed by: {hostname})"

            self.send_response(200)
            self.send_header('Content-type', 'text/plain; charset=utf-8')
            self.end_headers()
            self.wfile.write(message.encode('utf-8'))
        except Exception as e:
            self.send_response(500)
            self.end_headers()
            error_msg = f"Redis Error: {str(e)}"
            self.wfile.write(error_msg.encode('utf-8'))

server = HTTPServer(('0.0.0.0', 8080), SimpleHandler)
print("Python Redis App is running...")
server.serve_forever()
