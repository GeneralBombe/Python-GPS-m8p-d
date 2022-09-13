// generated from rosidl_generator_c/resource/idl__functions.h.em
// with input from gps_msgs:msg/GPSFix.idl
// generated code does not contain a copyright notice

#ifndef GPS_MSGS__MSG__DETAIL__GPS_FIX__FUNCTIONS_H_
#define GPS_MSGS__MSG__DETAIL__GPS_FIX__FUNCTIONS_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stdlib.h>

#include "rosidl_runtime_c/visibility_control.h"
#include "gps_msgs/msg/rosidl_generator_c__visibility_control.h"

#include "gps_msgs/msg/detail/gps_fix__struct.h"

/// Initialize msg/GPSFix message.
/**
 * If the init function is called twice for the same message without
 * calling fini inbetween previously allocated memory will be leaked.
 * \param[in,out] msg The previously allocated message pointer.
 * Fields without a default value will not be initialized by this function.
 * You might want to call memset(msg, 0, sizeof(
 * gps_msgs__msg__GPSFix
 * )) before or use
 * gps_msgs__msg__GPSFix__create()
 * to allocate and initialize the message.
 * \return true if initialization was successful, otherwise false
 */
ROSIDL_GENERATOR_C_PUBLIC_gps_msgs
bool
gps_msgs__msg__GPSFix__init(gps_msgs__msg__GPSFix * msg);

/// Finalize msg/GPSFix message.
/**
 * \param[in,out] msg The allocated message pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_gps_msgs
void
gps_msgs__msg__GPSFix__fini(gps_msgs__msg__GPSFix * msg);

/// Create msg/GPSFix message.
/**
 * It allocates the memory for the message, sets the memory to zero, and
 * calls
 * gps_msgs__msg__GPSFix__init().
 * \return The pointer to the initialized message if successful,
 * otherwise NULL
 */
ROSIDL_GENERATOR_C_PUBLIC_gps_msgs
gps_msgs__msg__GPSFix *
gps_msgs__msg__GPSFix__create();

/// Destroy msg/GPSFix message.
/**
 * It calls
 * gps_msgs__msg__GPSFix__fini()
 * and frees the memory of the message.
 * \param[in,out] msg The allocated message pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_gps_msgs
void
gps_msgs__msg__GPSFix__destroy(gps_msgs__msg__GPSFix * msg);

/// Check for msg/GPSFix message equality.
/**
 * \param[in] lhs The message on the left hand size of the equality operator.
 * \param[in] rhs The message on the right hand size of the equality operator.
 * \return true if messages are equal, otherwise false.
 */
ROSIDL_GENERATOR_C_PUBLIC_gps_msgs
bool
gps_msgs__msg__GPSFix__are_equal(const gps_msgs__msg__GPSFix * lhs, const gps_msgs__msg__GPSFix * rhs);

/// Copy a msg/GPSFix message.
/**
 * This functions performs a deep copy, as opposed to the shallow copy that
 * plain assignment yields.
 *
 * \param[in] input The source message pointer.
 * \param[out] output The target message pointer, which must
 *   have been initialized before calling this function.
 * \return true if successful, or false if either pointer is null
 *   or memory allocation fails.
 */
ROSIDL_GENERATOR_C_PUBLIC_gps_msgs
bool
gps_msgs__msg__GPSFix__copy(
  const gps_msgs__msg__GPSFix * input,
  gps_msgs__msg__GPSFix * output);

/// Initialize array of msg/GPSFix messages.
/**
 * It allocates the memory for the number of elements and calls
 * gps_msgs__msg__GPSFix__init()
 * for each element of the array.
 * \param[in,out] array The allocated array pointer.
 * \param[in] size The size / capacity of the array.
 * \return true if initialization was successful, otherwise false
 * If the array pointer is valid and the size is zero it is guaranteed
 # to return true.
 */
ROSIDL_GENERATOR_C_PUBLIC_gps_msgs
bool
gps_msgs__msg__GPSFix__Sequence__init(gps_msgs__msg__GPSFix__Sequence * array, size_t size);

/// Finalize array of msg/GPSFix messages.
/**
 * It calls
 * gps_msgs__msg__GPSFix__fini()
 * for each element of the array and frees the memory for the number of
 * elements.
 * \param[in,out] array The initialized array pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_gps_msgs
void
gps_msgs__msg__GPSFix__Sequence__fini(gps_msgs__msg__GPSFix__Sequence * array);

/// Create array of msg/GPSFix messages.
/**
 * It allocates the memory for the array and calls
 * gps_msgs__msg__GPSFix__Sequence__init().
 * \param[in] size The size / capacity of the array.
 * \return The pointer to the initialized array if successful, otherwise NULL
 */
ROSIDL_GENERATOR_C_PUBLIC_gps_msgs
gps_msgs__msg__GPSFix__Sequence *
gps_msgs__msg__GPSFix__Sequence__create(size_t size);

/// Destroy array of msg/GPSFix messages.
/**
 * It calls
 * gps_msgs__msg__GPSFix__Sequence__fini()
 * on the array,
 * and frees the memory of the array.
 * \param[in,out] array The initialized array pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_gps_msgs
void
gps_msgs__msg__GPSFix__Sequence__destroy(gps_msgs__msg__GPSFix__Sequence * array);

/// Check for msg/GPSFix message array equality.
/**
 * \param[in] lhs The message array on the left hand size of the equality operator.
 * \param[in] rhs The message array on the right hand size of the equality operator.
 * \return true if message arrays are equal in size and content, otherwise false.
 */
ROSIDL_GENERATOR_C_PUBLIC_gps_msgs
bool
gps_msgs__msg__GPSFix__Sequence__are_equal(const gps_msgs__msg__GPSFix__Sequence * lhs, const gps_msgs__msg__GPSFix__Sequence * rhs);

/// Copy an array of msg/GPSFix messages.
/**
 * This functions performs a deep copy, as opposed to the shallow copy that
 * plain assignment yields.
 *
 * \param[in] input The source array pointer.
 * \param[out] output The target array pointer, which must
 *   have been initialized before calling this function.
 * \return true if successful, or false if either pointer
 *   is null or memory allocation fails.
 */
ROSIDL_GENERATOR_C_PUBLIC_gps_msgs
bool
gps_msgs__msg__GPSFix__Sequence__copy(
  const gps_msgs__msg__GPSFix__Sequence * input,
  gps_msgs__msg__GPSFix__Sequence * output);

#ifdef __cplusplus
}
#endif

#endif  // GPS_MSGS__MSG__DETAIL__GPS_FIX__FUNCTIONS_H_
