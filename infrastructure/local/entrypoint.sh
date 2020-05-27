#!/bin/bash


if [ $1 == "deploy" ]
then
  python3 -u wait_for_local_stack.py
  
  terraform init
  terraform apply --auto-approve
fi

