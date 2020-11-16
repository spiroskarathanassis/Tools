/*
 * ----- Minify files from "entry" folder -----
 * @param entry : string
 *   folder name directory
 *
 * @returns exportModules: array
 *   returns array of key-value pair as the same file-name
 *   e.g. ['file_1': 'file_1', 'file_2': 'file_2']
 * 
 */

const glob = require('glob');

const moduleStructure = (entry) => {
  if (!entry) {
    console.log('Directory of modules is not exist.');
    return;
  }

  let exportModules = {};
  let modules = [];
  // regex to remove the rest of file name
  const regexDir = entry.replace(/\*.*/, '');
  const regexFile = entry.replace(/.*\*/, '');
  // create array with al js from entry folder
  modules = glob.sync(entry);
  
  // extract obj as {name: directory} for each file   
  modules.forEach(el => {
    let name = el
      .replace(regexDir, '')
      .replace(regexFile, '');

    exportModules[name] = el;
    console.log(name);
  });

  return exportModules;
}

module.exports = moduleStructure;
