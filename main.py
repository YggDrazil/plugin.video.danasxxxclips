# -*- coding: utf-8 -*-
# Module: default
# Author: Roman V. M.
# Created on: 28.11.2014
# License: GPL v.3 https://www.gnu.org/copyleft/gpl.html

import sys
from urllib import urlencode
from urlparse import parse_qsl
import xbmcgui
import xbmcplugin

# Get the plugin url in plugin:// notation.
_url = sys.argv[0]
# Get the plugin handle as an integer number.
_handle = int(sys.argv[1])

# Free sample videos are provided by www.vidsplay.com
# Here we use a fixed set of properties simply for demonstrating purposes
# In a "real life" plugin you will need to get info and links to video files/streams
# from some web-site or online service.
VIDEOS = {'Private Specials 162': [{'name': 'Mirror #1',
                       'thumb': 'https://s1.imgcloud.pw/2017/03/25/15090c9.jpg',
                       'video': 'https://oql957.oloadcdn.net/dl/l/LGd5lz1eAFAoi6My/KdlK_vxZvls/Private+Specials+162+Hot+Hitchhikers.mp4',
                       'genre': 'Full'}
                      ],
           'Au Pair Teenies': [{'name': 'Mirror #1',
                      'thumb': 'http://imagez.host/di/2H4Q/Au_Pair_Teenies_-_Neugierig_Auf_Geile_S%C3%BCnden.jpg',
                      'video': 'https://openload.co/embed/vTS4rQ-GzoU/Au.Pair.Teenies.Neugierig.Auf.Geile.Sunden.avi.mp4',
                      'genre': 'Full'}
                     ],
          'Arena Extreme #61': [{'name': 'Mirror #1',
                      'thumb': 'http://imagez.host/di/S9MN/Arena_Extrem_61_-_Sperma_Macchiato.jpg',
                      'video': 'https://openload.co/embed/dprZBv8qdd4/Arena.Extrem.61.Sperma.Macchiato.avi.mp4',
                      'genre': 'Full'}
                     ],
            'Gangstas Paradise': [{'name': 'Mirror #1',
                      'thumb': 'http://imagez.host/di/ZO5W/Gangsta´s_Paradise.jpg',
                      'video': 'https://openload.co/embed/XXjk3m09rN8/Gangstas.Paradise.avi.mp4',
                      'genre': 'Full'}
                     ],
          'Ich bin Jung und brauche das Geld #47': [{'name': 'Mirror #1',
                      'thumb': 'http://imagez.host/di/N4DE/Ich_Bin_Jung_Und_Brauche_Das_Geld_47.jpg',
                      'video': 'https://1fhjloz.oloadcdn.net/dl/l/NQ6F4ZH_5iN8jRit/bMfVs5o1AQU/Virgins+Of+The+Screen+5.mp4',
                      'genre': 'Full'}
                     ],
          'Schleich Connection': [{'name': 'Mirror #1',
                      'thumb': 'http://imagez.host/di/AJ0H/Scheich_Connection_-_Gebohrt_nach_Fotzensaft.jpg',
                      'video': 'https://openload.co/embed/OeFMxfCoFak/Scheich_Connection_-_Gebohrt_nach_Fotzensaft.avi.mp4',
                      'genre': 'Full'}
                     ],
          'Unter Deutschen Daechern': [{'name': 'Mirror #1',
                      'thumb': 'https://picload.org/image/rdcraidp/2.jpg',
                      'video': 'https://openload.co/embed/1Tdabm4k5lo/Deutscher_Originalton_Partnertausch.mp4',
                      'genre': 'Full'}
                     ],
          'Wiener Glut: Schubertgasse #3': [{'name': 'Mirror #1',
                      'thumb': 'http://imagez.host/di/VJCA/Wiener_Glut_Schubertgasse_Sex,_Teil_3.jpg',
                      'video': 'https://openload.co/embed/w3fKIyIyAdQ/Wiener_Glut_3.avi.mp4',
                      'genre': 'Full'}
                     ],
          'Freche Goeren #8': [{'name': 'Mirror #1',
                      'thumb': 'http://imagez.host/di/UBIV/Freche_G%C3%B6ren_8.jpg',
                      'video': 'https://openload.co/embed/I3vz21JV_O0/Freche_Goeren_8.mp4',
                      'genre': 'Full'}
                     ],
            'Blutjunge Spermafresser': [{'name': 'Mirror #1',
                      'thumb': 'http://img162.imagetwist.com/th/14634/oljqehnb1lg4.jpg',
                      'video': 'https://openload.co/embed/8QpQ8x750nk/Blutjunge_Spermafresser.avi.mp4',
                      'genre': 'Full'}
                     ],
          'Achtzehneinhalb #18': [{'name': 'Mirror #1',
                      'thumb': 'http://imagez.host/di/8USE/Achtzehneinhalb_18.jpg',
                      'video': 'https://openload.co/embed/5d2O-hPUECw/Achtzehneinhalb_18.avi.mp4',
                      'genre': 'Full'}
                     ],
          'Pariser Goeren #1': [{'name': 'Mirror #1',
                      'thumb': 'http://imagez.host/di/OFBS/Pariser_G%C3%B6ren_1_-_Am_liebsten_in_den_Arsch,_Monsieur.jpg',
                      'video': 'https://openload.co/embed/jziCOL8FvE0/Pariser_G%C3%B6ren_1_-_Am_liebsten_in_den_Arsch%2C_Monsieur.avi.mp4',
                      'genre': 'Full'}
                     ],
          'Die Mega Titten': [{'name': 'Mirror #1',
                      'thumb': 'http://imagez.host/di/V0RI/Die_Mega_Titten.jpg',
                      'video': 'https://openload.co/embed/DbT7zibDgaE/Die_Megga_Titten.avi.mp4',
                      'genre': 'Full'}
                     ],
          'Watch Me Eat My Cream Pie #4': [{'name': 'Mirror #1',
                      'thumb': 'http://img116.imagetwist.com/th/14634/rqbwvxwc7v83.jpg',
                      'video': 'https://pgli2x.oloadcdn.net/dl/l/DYtqbtGvJFd6UBuz/hd9sQEh1Kwk/Watch+Me+Eat+My+Creampie+4.mp4',
                      'genre': 'Full'}
                     ],
          'Wet Inc. #2': [{'name': 'Mirror #1',
                      'thumb': 'http://img28.imagetwist.com/th/14634/tfwg6qjiaice.jpg#',
                      'video': 'https://1fgqfu3.oloadcdn.net/dl/l/tk33e9Urs2suj31Q/6oxqr4HrzWg/Wet+Inc+2.mp4',
                      'genre': 'Full'}
                     ],
            'Whats Crackin': [{'name': 'Mirror #1',
                      'thumb': 'http://img162.imagetwist.com/th/14634/oljqehnb1lg4.jpg',
                      'video': 'https://1fhjm2s.oloadcdn.net/dl/l/87QGibXudQljTNIx/Ny1OXa0sjqA/Whats+Crackin.mp4',
                      'genre': 'Full'}
                     ],
          'Marilyn - Kleine Spalten suesse Lippen': [{'name': 'Mirror #1',
                      'thumb': 'http://imagez.host/di/H0OO/Marilyn-Kleine_Spalten_suesse_Lippen.jpg',
                      'video': 'https://ph2dqs.oloadcdn.net/dl/l/VPIlZ66LjcJgVc5Y/M_XQqKxipvo/MarilynKleineSpaltensuesseLippen.avi.mp4',
                      'genre': 'Full'}
                     ],
          'Schmutzige Liebhaber': [{'name': 'Mirror #1',
                      'thumb': 'http://imagez.host/di/SHPA/Schmutzige_Liebhaber.png',
                      'video': 'https://ph2dqt.oloadcdn.net/dl/l/zgn_lHQaKVmogqvL/KcjhDbOUlNA/Schmutzige+Liebhaber.mp4',
                      'genre': 'Full'}
                     ],
          'Meet my Ass #9': [{'name': 'Mirror #1',
                      'thumb': 'http://img66.imagetwist.com/th/14658/o41bbbtbfzes.jpg',
                      'video': 'https://1fiag16.oloadcdn.net/dl/l/oq-DQrGwhnvYzykT/ioa4KmKEW4w/Meat+My+Ass+9+%28NEWPORT+DISTRIBUTING.mp4',
                      'genre': 'Full'}
                     ],
          'Little Girls and Cream Pies': [{'name': 'Mirror #1',
                      'thumb': 'https://s1.imgcloud.pw/2017/03/23/297475.jpg',
                      'video': 'https://1fiag0c.oloadcdn.net/dl/l/dBhqsvsqjfB7aWQ1/6pbAv0JWu-g/Litte+Girls+And+Cream+Pies+%28DIRTY+LAUNDRY+PICTURES.mp4',
                      'genre': 'Full'}
                     ],
          'Lets Play 2016': [{'name': 'Mirror #1',
                      'thumb': 'https://s1.imgcloud.pw/2017/03/19/13a4774.jpg',
                      'video': 'https://1fgm8gz.oloadcdn.net/dl/l/6YlZf8NYQP30QXNi/zNKOKjVsAZ4/Let%E2%80%99s+Play+.mp4',
                      'genre': 'Full'}
                     ],
            'Mia Khalifa #3': [{'name': 'Mirror #1',
                      'thumb': 'http://i.imgur.com/b0KiL2j.jpg',
                      'video': 'https://pgli3e.oloadcdn.net/dl/l/fN4eMAvKeeGGE71T/k2lY4ZljWfA/Mia+Khalifa+3+2017+.mp4',
                      'genre': 'Full'}
                     ],
          'New Girl in Town #18': [{'name': 'Mirror #1',
                      'thumb': 'https://img.adultdvdtalk.com/4b3df6e03f03491792',
                      'video': 'https://oqbkhy.oloadcdn.net/dl/l/6UYNPKu9nccnwboh/wJo6j58vhJY/New+Girl+In+Town+18+.mp4',
                      'genre': 'Full'}
                     ],
          'Big Dick in a Little Chick #2': [{'name': 'Mirror #1',
                      'thumb': 'http://i1.imagetwist.com/i/14655/6s00i6auaq8g.jpeg/8b69b1bff962.jpeg',
                      'video': 'https://oql955.oloadcdn.net/dl/l/wzKsrKGOm0ZyrLL7/LWnHmP5PsFI/Big+Dick+In+A+Little+Chick+2+%28Digital+Sin%2FWEBRip%2FSD.mp4',
                      'genre': 'Full'}
                     ],
          'Meet my Ass #9': [{'name': 'Mirror #1',
                      'thumb': 'http://img66.imagetwist.com/th/14658/o41bbbtbfzes.jpg',
                      'video': 'https://1fiag16.oloadcdn.net/dl/l/oq-DQrGwhnvYzykT/ioa4KmKEW4w/Meat+My+Ass+9+%28NEWPORT+DISTRIBUTING.mp4',
                      'genre': 'Full'}
                     ],
          'Petite HD Porn #15': [{'name': 'Mirror #1',
                      'thumb': 'http://img66.imagetwist.com/th/14473/2ojlqo5jmdyr.jpg',
                      'video': 'https://1fhjm3e.oloadcdn.net/dl/l/zbv5nZHstBlAdt44/6awDt-UY-CE/Petite+HD+Porn+15%3A+One+Track+Mind+%282017%2FNubiles%2FWEBRip%2FSD.mp4',
                      'genre': 'Full'}
                     ],
          'BJ Battles #2': [{'name': 'Mirror #1',
                      'thumb': 'http://i1.imagetwist.com/th/14682/o7fivf9jbja6.jpg',
                      'video': 'https://1fhjm34.oloadcdn.net/dl/l/QMWqaidhF9T9JY0i/ahP8rPMR96s/BJ+Battles+2+%282017%2FElegant+Angel%2FDVDRip.mp4',
                      'genre': 'Full'}
                     ],
          'The Key': [{'name': 'Mirror #1',
                      'thumb': 'http://img28.imagetwist.com/th/14697/z5brs0bbwtj7.jpg',
                      'video': 'https://1fgm902.oloadcdn.net/dl/l/T7CzbmZP0tRLjG8H/ZRq1cfpyGAk/The+Key+%28Wicked+Pictures%29.mp4',
                      'genre': 'Full'}
                     ],
          'New to the Game #10': [{'name': 'Mirror #1',
                      'thumb': 'http://img162.imagetwist.com/th/14683/k4ivvzscgp4m.jpg',
                      'video': 'https://1fgqftq.oloadcdn.net/dl/l/KSExJemKaat5rh9h/rZ_Is9t3org/New+To+The+Game+10.mp4',
                      'genre': 'Full'}
                     ],
          'Sperm Sponges #2': [{'name': 'Mirror #1',
                      'thumb': 'http://img162.imagetwist.com/th/14683/sspng9v8n40p.jpg',
                      'video': 'https://1fgm8kl.oloadcdn.net/dl/l/C4ipKnsx0XzIo4un/rUtYxEgh7co/Sperm+Sponges+2.mp4',
                      'genre': 'Full'}
                     ],
          'Teen Brazil #2': [{'name': 'Mirror #1',
                      'thumb': 'http://img162.imagetwist.com/th/14634/6lc84v7kpvg1.jpg',
                      'video': 'https://1fhjlp2.oloadcdn.net/dl/l/z3OWGBuvF1RYcvuL/5-NzaL-9fWQ/Teen+Brazil+2mp4',
                      'genre': 'Full'}
                     ],
          'Teen Brazil #3': [{'name': 'Openload.co',
                      'thumb': 'http://img116.imagetwist.com/th/14634/iphq5kcij4be.jpg',
                      'video': 'https://openload.co/embed/HtHkMpfbFcQ/Teen_Brazil_3.mp4',
                      'genre': 'Full'}
                     ],
          'Tempt Me': [{'name': 'Mirror #1',
                      'thumb': 'http://img66.imagetwist.com/th/14634/zjf07ic1ednx.jpg',
                      'video': 'https://oqt1p2.oloadcdn.net/dl/l/WqcTlKUBGAI-lWx2/pcfI_drEvUA/Tempt+Me.mp4',
                      'genre': 'Full'}
                     ],
          'Virgins of the Screen #5': [{'name': 'Openload.co',
                      'thumb': 'http://img28.imagetwist.com/th/14634/ke31hcwf0gu7.jpg',
                      'video': 'https://openload.co/embed/bMfVs5o1AQU/Virgins_Of_The_Screen_5.mp4',
                      'genre': 'Full'}
                     ],
            'Teens Love Huge Cocks 12': [{'name': 'Mirror #1',
                      'thumb': 'https://movie4k.org/thumbs/cover-7646955-Teens-Love-Huge-Cocks-12-movie4k-film.jpg',
                      'video': 'https://1fiagel.oloadcdn.net/dl/l/p-y5MF9N7G5wZuG2/zGdeiEyQpmc/Teens+Love+Huge+Cocks+12.mp4',
                      'genre': 'Teen'}
                     ]}


def get_url(**kwargs):
    """
    Create a URL for calling the plugin recursively from the given set of keyword arguments.

    :param kwargs: "argument=value" pairs
    :type kwargs: dict
    :return: plugin call URL
    :rtype: str
    """
    return '{0}?{1}'.format(_url, urlencode(kwargs))


def get_categories():
    """
    Get the list of video categories.

    Here you can insert some parsing code that retrieves
    the list of video categories (e.g. 'Movies', 'TV-shows', 'Documentaries' etc.)
    from some site or server.

    .. note:: Consider using `generator functions <https://wiki.python.org/moin/Generators>`_
        instead of returning lists.

    :return: The list of video categories
    :rtype: list
    """
    return VIDEOS.iterkeys()


def get_videos(category):
    """
    Get the list of videofiles/streams.

    Here you can insert some parsing code that retrieves
    the list of video streams in the given category from some site or server.

    .. note:: Consider using `generators functions <https://wiki.python.org/moin/Generators>`_
        instead of returning lists.

    :param category: Category name
    :type category: str
    :return: the list of videos in the category
    :rtype: list
    """
    return VIDEOS[category]


def list_categories():
    """
    Create the list of video categories in the Kodi interface.
    """
    # Get video categories
    categories = get_categories()
    # Iterate through categories
    for category in categories:
        # Create a list item with a text label and a thumbnail image.
        list_item = xbmcgui.ListItem(label=category)
        # Set graphics (thumbnail, fanart, banner, poster, landscape etc.) for the list item.
        # Here we use the same image for all items for simplicity's sake.
        # In a real-life plugin you need to set each image accordingly.
        list_item.setArt({'thumb': VIDEOS[category][0]['thumb'],
                          'icon': VIDEOS[category][0]['thumb'],
                          'fanart': VIDEOS[category][0]['thumb']})
        # Set additional info for the list item.
        # Here we use a category name for both properties for for simplicity's sake.
        # setInfo allows to set various information for an item.
        # For available properties see the following link:
        # http://mirrors.xbmc.org/docs/python-docs/15.x-isengard/xbmcgui.html#ListItem-setInfo
        list_item.setInfo('video', {'title': category, 'genre': category})
        # Create a URL for a plugin recursive call.
        # Example: plugin://plugin.video.example/?action=listing&category=Animals
        url = get_url(action='listing', category=category)
        # is_folder = True means that this item opens a sub-list of lower level items.
        is_folder = True
        # Add our item to the Kodi virtual folder listing.
        xbmcplugin.addDirectoryItem(_handle, url, list_item, is_folder)
    # Add a sort method for the virtual folder items (alphabetically, ignore articles)
    xbmcplugin.addSortMethod(_handle, xbmcplugin.SORT_METHOD_LABEL_IGNORE_THE)
    # Finish creating a virtual folder.
    xbmcplugin.endOfDirectory(_handle)


def list_videos(category):
    """
    Create the list of playable videos in the Kodi interface.

    :param category: Category name
    :type category: str
    """
    # Get the list of videos in the category.
    videos = get_videos(category)
    # Iterate through videos.
    for video in videos:
        # Create a list item with a text label and a thumbnail image.
        list_item = xbmcgui.ListItem(label=video['name'])
        # Set additional info for the list item.
        list_item.setInfo('video', {'title': video['name'], 'genre': video['genre']})
        # Set graphics (thumbnail, fanart, banner, poster, landscape etc.) for the list item.
        # Here we use the same image for all items for simplicity's sake.
        # In a real-life plugin you need to set each image accordingly.
        list_item.setArt({'thumb': video['thumb'], 'icon': video['thumb'], 'fanart': video['thumb']})
        # Set 'IsPlayable' property to 'true'.
        # This is mandatory for playable items!
        list_item.setProperty('IsPlayable', 'true')
        # Create a URL for a plugin recursive call.
        # Example: plugin://plugin.video.example/?action=play&video=http://www.vidsplay.com/vids/crab.mp4
        url = get_url(action='play', video=video['video'])
        # Add the list item to a virtual Kodi folder.
        # is_folder = False means that this item won't open any sub-list.
        is_folder = False
        # Add our item to the Kodi virtual folder listing.
        xbmcplugin.addDirectoryItem(_handle, url, list_item, is_folder)
    # Add a sort method for the virtual folder items (alphabetically, ignore articles)
    xbmcplugin.addSortMethod(_handle, xbmcplugin.SORT_METHOD_LABEL_IGNORE_THE)
    # Finish creating a virtual folder.
    xbmcplugin.endOfDirectory(_handle)


def play_video(path):
    """
    Play a video by the provided path.

    :param path: Fully-qualified video URL
    :type path: str
    """
    # Create a playable item with a path to play.
    play_item = xbmcgui.ListItem(path=path)
    # Pass the item to the Kodi player.
    xbmcplugin.setResolvedUrl(_handle, True, listitem=play_item)


def router(paramstring):
    """
    Router function that calls other functions
    depending on the provided paramstring

    :param paramstring: URL encoded plugin paramstring
    :type paramstring: str
    """
    # Parse a URL-encoded paramstring to the dictionary of
    # {<parameter>: <value>} elements
    params = dict(parse_qsl(paramstring))
    # Check the parameters passed to the plugin
    if params:
        if params['action'] == 'listing':
            # Display the list of videos in a provided category.
            list_videos(params['category'])
        elif params['action'] == 'play':
            # Play a video from a provided URL.
            play_video(params['video'])
        else:
            # If the provided paramstring does not contain a supported action
            # we raise an exception. This helps to catch coding errors,
            # e.g. typos in action names.
            raise ValueError('Invalid paramstring: {0}!'.format(paramstring))
    else:
        # If the plugin is called from Kodi UI without any parameters,
        # display the list of video categories
        list_categories()


if __name__ == '__main__':
    # Call the router function and pass the plugin call parameters to it.
    # We use string slicing to trim the leading '?' from the plugin call paramstring
    router(sys.argv[2][1:])
