# $FreeBSD$

PORTNAME=	seafobj
PORTVERSION=	3.0.4
PORTREVISION=	1
CATEGORIES=	www python
PKGNAMEPREFIX=	${PYTHON_PKGNAMEPREFIX}

MAINTAINER=	yan_jingfeng@yahoo.com
COMMENT=	Python library for accessing seafile data model

LICENSE=	APACHE20

USE_GITHUB=	yes
GH_ACCOUNT=	haiwen
GH_TAGNAME=	v${PORTVERSION}-server-testing
GH_COMMIT=	58a4346

NO_BUILD=	yes
USES=		python:2

HAIWENDIR=	www/haiwen
SEAFILE_SERVER=	${HAIWENDIR}/seafile-server
SEAHUBDIR=	${SEAFILE_SERVER}/seahub
SITEPACKAGEDIR=	${SEAHUBDIR}/thirdpart

SEAFILE_USERNAME?=	www
SEAFILE_GROUPNAME?=	${SEAFILE_USERNAME}

PLIST_SUB=	SEAFILE_USERNAME=${SEAFILE_USERNAME} \
		SEAFILE_GROUPNAME=${SEAFILE_GROUPNAME} \
		SEAFILE_SERVER=${SEAFILE_SERVER} \
		SEAHUBDIR=${SEAHUBDIR} \
		HAIWENDIR=${HAIWENDIR} \
		SITEPACKAGEDIR=${SITEPACKAGEDIR}

do-install:
	@${MKDIR} ${STAGEDIR}${PREFIX}/${SITEPACKAGEDIR}/seafobj
	(cd ${WRKSRC}/seafobj && \
		${PYTHON_CMD} ${PYTHON_LIBDIR}/compileall.py \
			-d ${WRKSRC}/seafobj \
			-f ${WRKSRC}/seafobj && \
		${PYTHON_CMD} -O ${PYTHON_LIBDIR}/compileall.py \
			-d ${WRKSRC}/seafobj \
			-f ${WRKSRC}/seafobj)
	(cd ${WRKSRC}/seafobj && \
		${COPYTREE_SHARE} . ${STAGEDIR}${PREFIX}/${SITEPACKAGEDIR}/seafobj)

.include <bsd.port.mk>
