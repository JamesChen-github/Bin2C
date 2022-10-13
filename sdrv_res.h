/**
 * @file sdrv_res.h
 *
 * Copyright (c) 2020 Semidrive Semiconductor.
 * All rights reserved.
 *
 * Description: sdrv res header.
 *
 * Revision History:
 * -----------------
 */

#ifndef SDRV_RES_H
#define SDRV_RES_H

#ifdef __cplusplus
extern "C" {
#endif

/*********************
 *      INCLUDES
 *********************/
#include <stdio.h>
#include <stdbool.h>

/*********************
 *      DEFINES
 *********************/

/**********************
 *      TYPEDEFS
 **********************/

/*sdrv res format*/
enum {
    SDRV_RES_FORMAT_UNKNOWN = 0,

    SDRV_RES_FORMAT_BIN_RAW,              /**< Contains the file as it is. Needs custom decoder function*/
    SDRV_RES_FORMAT_DATA_RAW,             /**< Contains the data as it is. NO Needs custom decoder function*/

};
typedef uint8_t sdrv_res_format_t;

/**
 * sdrv res header
 */
/* The first 8 bit is very important to distinguish the different source types.
 * For more info see `lv_img_get_src_type()` in lv_img.c
 * On big endian systems the order is reversed so cf and always_zero must be at
 * the end of the struct.
 * */
typedef struct {

    uint32_t rf : 5;          /* res format: See `sdrv_res_format_t`*/
    uint32_t always_zero : 3; /*It the upper bits of the first byte. Always zero to look like a
                                 non-printable character*/

    uint32_t reserved : 24; /*Reserved to be used later*/
} sdrv_res_header_t;

/** sdrv res header it is compatible with
 * the result from sdrv res converter utility*/
typedef struct {
    sdrv_res_header_t header;
    uint32_t data_size;
    const uint8_t * data;
} sdrv_res_dsc_t;

/**********************
 *      MACROS
 **********************/

#ifdef __cplusplus
} /* extern "C" */
#endif


#endif /*SDRV_RES_H*/