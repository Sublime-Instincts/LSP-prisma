import os
from lsp_utils import NpmClientHandler


def plugin_loaded():
    LspPrismaPlugin.setup()


def plugin_unloaded():
    LspPrismaPlugin.cleanup()


class LspPrismaPlugin(NpmClientHandler):
    package_name = __package__
    server_directory = "language-server"
    server_binary_path = os.path.join(
        server_directory,
        "node_modules",
        "@prisma", "language-server", "dist", "src", "bin.js"
    )
