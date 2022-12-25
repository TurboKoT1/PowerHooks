import requests

class Webhook:
  def send(url=None, username="PowerHook", content="Hello, PowerHooks!", embeds=None, avatar_url=None, tts=False, file=None):
    if url == None: raise RuntimeError("Вы не указали ссылку на вебхук!")
    elif requests.get(url).status_code != 200: raise RuntimeError("Вы указали ссылку на нерабочий вебхук!")
    else: requests.post(url, json={"username": username, "content": content, "embeds": embeds, "avatar_url": avatar_url, "tts": tts, "file": file})
  def delete(url=None):
    if url == None: raise RuntimeError("Вы не указали ссылку на вебхук!")
    elif requests.get(url).status_code != 200: raise RuntimeError("Вы указали ссылку на нерабочий вебхук!")
    else: requests.delete(url)