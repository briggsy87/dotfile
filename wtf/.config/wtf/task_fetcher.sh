#!/bin/sh

task export project:pwm status:pending | jq 'map({description: .description, status:.status})'