import link

link_name = "No link badge"
user_text = "get from input"
color = "orange"
badge_img_url = f"https://img.shields.io/static/v1?label=&message=web&nbsp;development&color={color}"
dummy_url = "https://"

badge_url = "![label](" + badge_img_url + ")]"

link.xref_links.update({link_name: (badge_url, dummy_url)})