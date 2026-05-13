#include <sys/sysctl.h>
#include <IOKit/IOKitLib.h>
#include <errno.h>
#include <stdio.h>

#include "service_helpers.h"

#define MAX_RETRIES 10


/*
 * Helper method to find IOServices needed for testing. Use with T_ASSERT_POSIX_SUCCESS(...)
 */
int
IOTestServiceFindService(const char * name, io_service_t * serviceOut)

