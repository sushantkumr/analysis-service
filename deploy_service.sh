#!/bin/bash
gcloud compute scp ../analysis-service/project/ analysis-service:/opt/analysis-service/ --recurse
