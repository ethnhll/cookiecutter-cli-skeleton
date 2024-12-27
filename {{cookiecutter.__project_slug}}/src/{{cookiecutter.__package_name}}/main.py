import typer
from typer import Typer
from config.schemas import ApplicationSettings


def build_application(app_settings: ApplicationSettings) -> Typer:
    """
    TODO: complete documentation

    :param app_settings:
    :return:
    """
    app = Typer()
    # TODO: add subcommands here
    return app


def main():
    app = build_application(app_settings=ApplicationSettings())
    typer.run(app)


if __name__ == '__main__':
    main()
