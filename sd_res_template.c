#include "sdrv_res.h"

#ifndef SDRV_RES_ATTRIBUTE_MEM_ALIGN
#define SDRV_RES_ATTRIBUTE_MEM_ALIGN
#endif

#define SDRV_RES_{NAME_UPPER}_RF SDRV_RES_FORMAT_BIN_RAW //SDRV_RES_FORMAT_DATA_RAW

const SDRV_RES_ATTRIBUTE_MEM_ALIGN uint8_t sdrv_res_{NAME_LOWER}_map[] = {
#if SDRV_RES_{NAME_UPPER}_RF == SDRV_RES_FORMAT_BIN_RAW
{BIN_RAW}
#endif
#if SDRV_RES_{NAME_UPPER}_RF == SDRV_RES_FORMAT_DATA_RAW
{DATA_RAW}
#endif
};

const sdrv_res_dsc_t sdrv_res_{NAME_LOWER} = {
  .header.always_zero = SDRV_RES_{NAME_UPPER}_RF,
  .header.rf = 0,
#if SDRV_RES_{NAME_UPPER}_RF == SDRV_RES_FORMAT_BIN_RAW
  .data_size = {DATA_SIZE},
#endif
#if SDRV_RES_{NAME_UPPER}_RF == SDRV_RES_FORMAT_DATA_RAW
  .data_size = {DATA_SIZE},
#endif
  .data = sdrv_res_{NAME_LOWER}_map,
};
