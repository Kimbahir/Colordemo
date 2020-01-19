from app import app
import os


def rgb2hex(r, g, b):
    return "#{:02x}{:02x}{:02x}".format(r, g, b)


@app.route("/")
def home():
    app.config['kba_counter'] += 1
    r, g, b = app.config['kba_color']

    return f"""
        <html>
            <head>
                <title>K8s demo</title>
                <meta http-equiv="refresh" content="1" />
            </head>
            <body style="background-color: {rgb2hex(r,g,b)}">
                <table style="border:0">
                    <tr>
                        <td style="background-color: white">Hostname: </td>
                        <td style="background-color: white">{app.config['kba_hostname']}</td>
                    </tr>
                    <tr>
                        <td style="background-color: white">Visits: </td>
                        <td style="background-color: white">{app.config['kba_counter']}</td>
                    </tr>
                </table>
            </body>
        </html>
    """
