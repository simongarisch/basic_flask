from waitress import serve
import index
 
if __name__ == '__main__':
   serve(index.app, host='0.0.0.0', port=81)
