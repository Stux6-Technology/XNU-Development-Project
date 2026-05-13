#include <sys/sysctl.h>
#include <IOKit/IOKitLib.h>
#include <errno.h>
#include <stdio.h>

#include "service_helpers.h"

#define MAX_RETRIES 10

