def get_journal_statistics():
    # returns {journal_id -> (total_views, total_downloads)}
    summary = {}
    publications = Publication.objects.all().prefetch_related('hit')
    for pub in publications:
        summary[pub.journal_id] = (
            pub.hit_set.filter(action=Hit.PAGEVIEW).count(),
            pub.hit_set.filter(action=Hit.DOWNLOAD).count()
        )

    return summary