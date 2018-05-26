import web
import thermo_routes


urls = (
    '/thermometers', thermo_routes.app
)

def main():
    app = web.application(urls, locals())
    app.run()  

if __name__ == "__main__":
    main()
