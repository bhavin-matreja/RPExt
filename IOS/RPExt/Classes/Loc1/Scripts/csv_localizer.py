import datetime
import os
import sys
import csv
import json
import genstruct


NOW = datetime.datetime.now().strftime("%Y-%m-%d, %H:%M")
CURRENT_DIR = os.path.dirname(__file__)

def main():
  print "Localizing..."
  with open(os.path.join(CURRENT_DIR, "settings.json")) as setting_file:
    setting = json.load(setting_file)

    PLATFORM = setting["PLATFORM"]
    IN_PATH = setting["IN_PATH"]
    OUT_PATH = setting["OUT_PATH"]
    LANG_KEYS = setting["LANG_KEYS"]
    BASE_STRINGS_PATH = setting["BASE_STRINGS_PATH"]
    if BASE_STRINGS_PATH == "currentdir":
      print "Detect currentdir -> \n  " + CURRENT_DIR
      BASE_STRINGS_PATH = CURRENT_DIR

    GEN_STRUCT_IF_IOS = setting["GEN_STRUCT_IF_IOS"]

    print "Platform: {0}".format(PLATFORM)
    print "In path: {0}".format(IN_PATH)
    print "Out path: {0}".format(OUT_PATH)
    print "Lang keys: {0}".format(LANG_KEYS)
    print "------------------------------------\nSTART..."

    if PLATFORM == "ios":
      localize_ios(BASE_STRINGS_PATH, IN_PATH, OUT_PATH, LANG_KEYS)
    else:
      localize_android(BASE_STRINGS_PATH, IN_PATH, OUT_PATH, LANG_KEYS)

    print 'DONE LOCALIZING.'
    print '\n\n'

    if PLATFORM.lower() == "ios" and GEN_STRUCT_IF_IOS:
      genstruct.main()

def localize_ios(BASE_PATH, IN_PATH, OUT_PATH, LANG_KEYS):

  base_out_dir = os.path.join(BASE_PATH, OUT_PATH)
  # top most
  if not os.path.exists(base_out_dir):
      os.makedirs(base_out_dir)

  # each languages
  for lang in LANG_KEYS:
    lang_path = os.path.join(base_out_dir, "{0}.lproj/".format(lang))
    if not os.path.exists(lang_path):
      os.makedirs(lang_path)


  full_out_paths = [os.path.join(base_out_dir, "{0}.lproj/".format(langKey) + "Localizable.strings") for langKey in LANG_KEYS]
  allwrites = [open(out_path, 'w') for out_path in full_out_paths]

  for dirname, dirnames, filenames in os.walk(os.path.join(CURRENT_DIR, IN_PATH)):

    [fwrite.write('\n\n\n/*  AUTO-GENERATED: {timestamp} */\n\n'.format(timestamp=NOW)) for fwrite in allwrites]

    for f in filenames:
      filename, ext = os.path.splitext(f)
      if ext != '.csv':
        continue

      fullpath = os.path.join(dirname, f)
      print 'Localizing: ' + filename + ' ...'

      with open(fullpath, 'rb') as csvfile:
        [fwrite.write('\n\n\n/*  {0}  */\n\n'.format(filename)) for fwrite in allwrites]

        reader = csv.reader(csvfile, delimiter=',')

        iterrows = iter(reader);
        next(iterrows) # skip first line (it is header).

        for row in iterrows:
          row_key = row[0].replace(" ", "")
          # comment
          if row_key[:2] == '//':
            continue

          row_values = [row[i+1] for i in range(len(LANG_KEYS))]

          # if any row is empty, skip it!
          if any([value == "" for value in row_values]):
            continue
          [fwrite.write('"{domain}_{key}" = "{lang}";\n'.format(domain=filename, key=row_key, lang=row_values[idx])) for idx, fwrite in enumerate(allwrites)]
  [fwrite.close() for fwrite in allwrites]


def localize_android(BASE_PATH, IN_PATH, OUT_PATH, LANG_KEYS):
  base_out_dir = os.path.join(BASE_PATH, OUT_PATH)
  # top most
  if not os.path.exists(base_out_dir):
      os.makedirs(base_out_dir)

  # each languages
  for lang in LANG_KEYS:
    lang_path = os.path.join(base_out_dir, "values-{0}/".format(lang))
    if not os.path.exists(lang_path):
      os.makedirs(lang_path)

  full_out_paths = [os.path.join(base_out_dir, "values-{0}/".format(langKey) + "strings.xml") for langKey in LANG_KEYS]
  allwrites = [open(out_path, 'w') for out_path in full_out_paths]

  for dirname, dirnames, filenames in os.walk(os.path.join(CURRENT_DIR, IN_PATH)):

    [fwrite.write('<?xml version="1.0" encoding="utf-8"?>\n') for fwrite in allwrites]
    [fwrite.write('<resources>') for fwrite in allwrites]

    for f in filenames:
      filename, ext = os.path.splitext(f)
      if ext != '.csv':
        continue
      fullpath = os.path.join(dirname, f)
      print 'Localizing: ' + filename + ' ...'

      with open(fullpath, 'rb') as csvfile:
        [fwrite.write('\n\n\n<!-- {0} -->\n\n'.format(filename)) for fwrite in allwrites]

        reader = csv.reader(csvfile, delimiter=',')

        iterrows = iter(reader);
        next(iterrows) # skip first line (it is header).
        for row in iterrows:
          row_key = row[0]

          # comment
          if row_key[:2] == '//':
            continue

          row_values = [row[i+1] for i in range(len(LANG_KEYS))]

          # if any row is empty, skip it!
          if any([value == "" for value in row_values]):
            continue

          [fwrite.write('\t<string name="{domain}_{key}">{lang}</string>\n'.format(domain=filename, key=row_key, lang=row_values[idx])) for idx, fwrite in enumerate(allwrites)]
    [fwrite.write('</resources>') for fwrite in allwrites]
  [fwrite.close() for fwrite in allwrites]


if __name__ == '__main__':
    main()