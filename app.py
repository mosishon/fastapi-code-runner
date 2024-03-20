import asyncio
import os
import sys
from tempfile import NamedTemporaryFile
from typing import Annotated

from fastapi import FastAPI, Form, UploadFile
from pydantic import BaseModel


class RunArgs(BaseModel):
    language: str
    args: str


app = FastAPI(debug=False)

# ADD MORE LANGUAGES
languages_run_configs = {
    "python": sys.executable+" {file_name} {args}",
}


def run_cmd(cmd: str) -> str:
    return os.popen(cmd).read()


@app.post("/run")
async def run(file: UploadFile, args: Annotated[str, Form()], language: Annotated[str, Form()]):
    if language not in languages_run_configs:
        return {"error": "language not found"}
    try:
        tf = NamedTemporaryFile(
            "w", suffix=".py", encoding="utf-8", delete=False)
        tf.write(file.file.read().decode())
        tf.close()
        cmd = languages_run_configs.get(language, "").format(
            file_name=tf.name, args=args)
        result = await asyncio.get_running_loop().run_in_executor(None, run_cmd, cmd)
        return {f"file-size": file.size, "result": result, "language": language, "file-path": tf.name}
    finally:
        os.remove(tf.name)
