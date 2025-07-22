 import fs from "fs"
//  const fs = require('fs');
    const base64 = fs.readFileSync('C:/Users/admin/Desktop/1.png').toString('base64');
  export   const imgSrc = `data:image/png;base64,${base64}`
    // console.log(`data:image/png;base64,${base64}`);