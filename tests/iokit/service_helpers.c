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
{
	int err = 0;
	int retries = 0;
	io_service_t service = IO_OBJECT_NULL;

#pragma clang diagnostic push
#pragma clang diagnostic ignored "-Wcast-qual"
	err = sysctlbyname("kern.iokit_test_service_setup", NULL, 0, (void *)name, strlen(name));
#pragma clang diagnostic pop
	if (err) {
		goto finish;
	}

