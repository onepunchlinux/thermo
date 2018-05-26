import web
import thermo_routes

def global_headers(handler):
    web.header('Content-Type', 'application/json')
    return handler()

urls = (
    '/thermometers', thermo_routes.app
)

def main():
    app = web.application(urls, locals())
    app.add_processor(global_headers)
    app.run()  


if __name__ == "__main__":
    main()
