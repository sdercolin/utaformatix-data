# UtaFormatix Data in TypeScript

[![npm version](https://badge.fury.io/js/utaformatix-data.svg)](https://badge.fury.io/js/utaformatix-data)

TypeScript definitions of [UtaFormatix Data Format](https://github.com/sdercolin/utaformatix-data).

## Install

This package is published on [npm](https://www.npmjs.com/package/utaformatix-data).

```bash
npm install utaformatix-data --save
```

## Example

```typescript
import { UfData, UtaFormatixDataVersion } from "utaformatix-data";

const jsonString = `...` // load from somewhere
const ufdata = JSON.parse(jsonString) as UfData;

console.log(ufdata.version); // version of the data loaded
console.log(UtaFormatixDataVersion); // version of the format used by current library version
console.log(ufdata.project.title); // access members
```
